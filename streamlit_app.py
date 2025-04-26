import streamlit as st
from utils import (
    add_glucose_reading,
    add_hba1c_reading,
    import_glucose_readings,
    search_glucose_readings,
    plot_glucose_trend,
    plot_glucose_with_rolling_avg,
    plot_hba1c_trend,
    plot_combined_trend,
    add_supply_item,
    update_supply_quantity,
    get_supplies,
    get_glucose_df,
    get_hba1c_df
)

st.set_page_config(page_title="Diabetes Tracker", layout="wide")
st.title("\ud83e\uddea Diabetes Tracker Dashboard")

# Sidebar Menu
menu = st.sidebar.selectbox("Menu", (
    "Home",
    "Add Glucose Reading",
    "Add HbA1c Reading",
    "Import Glucose CSV",
    "View Graphs",
    "Manage Supplies"
))

# Home Page
if menu == "Home":
    st.header("Welcome to Your Diabetes Tracker Web App!")
    st.markdown("Use the sidebar to add readings, import data, view graphs, and manage your supplies.")

# Add Glucose Reading
elif menu == "Add Glucose Reading":
    st.header("Add New Glucose Reading")
    with st.form("glucose_form"):
        date = st.date_input("Date")
        time = st.text_input("Time", value="-")
        level = st.number_input("Glucose Level", min_value=0.0, step=0.1)
        notes = st.text_input("Notes", value="-")
        submitted = st.form_submit_button("Submit")
        if submitted:
            message = add_glucose_reading(date.strftime("%d/%m/%Y"), time, level, notes)
            st.success(message)

# Add HbA1c Reading
elif menu == "Add HbA1c Reading":
    st.header("Add New HbA1c Reading")
    with st.form("hba1c_form"):
        date = st.date_input("Date")
        hba1c = st.number_input("HbA1c (%)", min_value=0.0, step=0.1)
        submitted = st.form_submit_button("Submit")
        if submitted:
            message = add_hba1c_reading(date.strftime("%d/%m/%Y"), hba1c)
            st.success(message)

# Import CSV
elif menu == "Import Glucose CSV":
    st.header("Import Glucose Readings from CSV")
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
    if uploaded_file is not None:
        with open("import_temp.csv", "wb") as f:
            f.write(uploaded_file.getbuffer())
        result = import_glucose_readings("import_temp.csv")
        st.success(result)

# View Graphs
elif menu == "View Graphs":
    st.header("Graphs and Trends")
    tab1, tab2, tab3 = st.tabs(["Glucose Trend", "HbA1c Trend", "Combined View"])

    with tab1:
        st.subheader("Glucose Levels Over Time")
        result = plot_glucose_with_rolling_avg()
        if result.startswith("Graph saved"):
            st.image("glucose_trend_avg_7d_30d.png")
        else:
            st.warning(result)

    with tab2:
        st.subheader("HbA1c Over Time")
        result = plot_hba1c_trend()
        if result.startswith("Graph saved"):
            st.image("hba1c_trend.png")
        else:
            st.warning(result)

    with tab3:
        st.subheader("Combined Glucose and HbA1c Trend")
        result = plot_combined_trend()
        if result.startswith("Graph saved"):
            st.image("combined_trend.png")
        else:
            st.warning(result)

# Manage Supplies
elif menu == "Manage Supplies":
    st.header("Manage Diabetic Supplies")
    tab1, tab2 = st.tabs(["View Supplies", "Update Supplies"])

    with tab1:
        st.subheader("Current Supplies")
        supplies_df = get_supplies()
        if supplies_df.empty:
            st.warning("No supplies recorded yet.")
        else:
            st.dataframe(supplies_df)

    with tab2:
        st.subheader("Add or Update Supply Items")
        with st.form("supply_form"):
            item_name = st.text_input("Item Name")
            quantity = st.number_input("Quantity", step=1)
            action = st.radio("Action", ("Add New Item", "Update Existing Item"))
            submitted = st.form_submit_button("Submit")
            if submitted:
                if action == "Add New Item":
                    message = add_supply_item(item_name, quantity)
                    st.success(message)
                else:
                    message = update_supply_quantity(item_name, quantity)
                    st.success(message)
