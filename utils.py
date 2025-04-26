import pandas as pd
import csv
import matplotlib.pyplot as plt
from datetime import datetime

# --- Glucose Functions ---

def add_glucose_reading(date, time, level, notes):
    with open("data/glucose_readings.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, time, level, notes])
    return "Glucose reading added successfully."

def import_glucose_readings(import_file):
    try:
        df = pd.read_csv(import_file)

        rows_to_add = []
        for _, row in df.iterrows():
            try:
                date = datetime.strptime(str(row["Date"]).strip(), "%d/%m/%Y").strftime("%d/%m/%Y")
                time = str(row["Time"]).strip() if not pd.isna(row["Time"]) else "-"
                level = float(row["Glucose Level"])
                notes = str(row["Notes"]).strip() if not pd.isna(row["Notes"]) else "-"
                rows_to_add.append([date, time, level, notes])
            except Exception:
                continue

        with open("data/glucose_readings.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows_to_add)

        return f"Imported {len(rows_to_add)} rows successfully."

    except FileNotFoundError:
        return "Import file not found."

def search_glucose_readings(by="date", value=None):
    try:
        df = pd.read_csv("data/glucose_readings.csv")
        df.columns = df.columns.str.strip().str.lower()
        df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y", errors="coerce")
    except FileNotFoundError:
        return pd.DataFrame()

    if by == "date":
        try:
            target_date = datetime.strptime(value, "%d/%m/%Y").date()
            result = df[df["date"].dt.date == target_date]
        except Exception:
            return pd.DataFrame()

    elif by == "level_above":
        result = df[df["level"] > float(value)]

    elif by == "level_below":
        result = df[df["level"] < float(value)]

    elif by == "note":
        result = df[df["notes"].str.contains(str(value), case=False, na=False)]

    else:
        return pd.DataFrame()

    return result

# --- Glucose Plotting ---

def plot_glucose_trend():
    try:
        df = pd.read_csv("data/glucose_readings.csv")
        df.columns = df.columns.str.strip().str.lower()
        df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y", errors="coerce")
    except FileNotFoundError:
        return "No readings found."

    if df.empty:
        return "No data to plot."

    df = df.sort_values("date")

    plt.figure(figsize=(10, 6))
    plt.plot(df["date"], df["level"], marker='o')
    plt.title("Blood Glucose Levels Over Time")
    plt.xlabel("Date")
    plt.ylabel("Glucose Level")
    plt.grid(True)
    plt.tight_layout()

    filename = "glucose_trend.png"
    plt.savefig(filename)
    return f"Graph saved as {filename}"

def plot_glucose_with_rolling_avg():
    try:
        df = pd.read_csv("data/glucose_readings.csv")
        df.columns = df.columns.str.strip().str.lower()
        df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y", errors="coerce")
    except FileNotFoundError:
        return "No readings found."

    if df.empty:
        return "No data to plot."

    df = df.sort_values("date")
    df = df.dropna(subset=["level"])

    df["7_day_avg"] = df["level"].rolling(window=7).mean()
    df["30_day_avg"] = df["level"].rolling(window=30).mean()

    plt.figure(figsize=(10, 6))
    plt.plot(df["date"], df["level"], marker='o', label="Glucose Level", alpha=0.6)
    plt.plot(df["date"], df["7_day_avg"], color='red', linewidth=2, label="7-Day Avg")
    plt.plot(df["date"], df["30_day_avg"], color='green', linewidth=2, label="30-Day Avg")

    plt.title("Blood Glucose with 7- and 30-Day Rolling Averages")
    plt.xlabel("Date")
    plt.ylabel("Glucose Level")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    filename = "glucose_trend_avg_7d_30d.png"
    plt.savefig(filename)
    return f"Graph saved as {filename}"

# --- HbA1c Functions ---

def plot_hba1c_trend():
    try:
        df = pd.read_csv("data/hba1c_readings.csv")
        df.columns = df.columns.str.strip().str.lower()
        df.rename(columns={"hba1c (%)": "hba1c"}, inplace=True)
        df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y", errors="coerce")
    except FileNotFoundError:
        return "No HbA1c file found."

    if df.empty or "hba1c" not in df.columns:
        return "No valid HbA1c data to plot."

    df = df.sort_values("date")

    plt.figure(figsize=(10, 6))
    plt.plot(df["date"], df["hba1c"], marker='o', color='purple', linewidth=2)
    plt.title("HbA1c Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("HbA1c (%)")
    plt.grid(True)
    plt.tight_layout()

    filename = "hba1c_trend.png"
    plt.savefig(filename)
    return f"Graph saved as {filename}"

def plot_combined_trend():
    try:
        glucose_df = pd.read_csv("data/glucose_readings.csv")
        glucose_df.columns = glucose_df.columns.str.strip().str.lower()
        glucose_df["date"] = pd.to_datetime(glucose_df["date"], format="%d/%m/%Y", errors="coerce")
        glucose_df = glucose_df.sort_values("date")
        glucose_df = glucose_df.dropna(subset=["level"])
        glucose_df["7_day_avg"] = glucose_df["level"].rolling(window=7).mean()
        glucose_df["30_day_avg"] = glucose_df["level"].rolling(window=30).mean()

        hba1c_df = pd.read_csv("data/hba1c_readings.csv")
        hba1c_df.columns = hba1c_df.columns.str.strip().str.lower()
        hba1c_df.rename(columns={"hba1c (%)": "hba1c"}, inplace=True)
        hba1c_df["date"] = pd.to_datetime(hba1c_df["date"], format="%d/%m/%Y", errors="coerce")
        hba1c_df = hba1c_df.sort_values("date")
    except Exception as e:
        return f"Error loading data: {e}"

    if glucose_df.empty or hba1c_df.empty:
        return "Not enough data to plot combined view."

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

    ax1.plot(glucose_df["date"], glucose_df["level"], label="Glucose Level", marker='o', alpha=0.6)
    ax1.plot(glucose_df["date"], glucose_df["7_day_avg"], color='red', linewidth=2, label="7-Day Avg")
    ax1.plot(glucose_df["date"], glucose_df["30_day_avg"], color='green', linewidth=2, label="30-Day Avg")
    ax1.set_title("Glucose Levels and Rolling Averages")
    ax1.set_ylabel("Glucose Level")
    ax1.grid(True)
    ax1.legend()

    ax2.plot(hba1c_df["date"], hba1c_df["hba1c"], label="HbA1c (%)", marker='o', color='purple', linewidth=2)
    for _, row in hba1c_df.iterrows():
        ax2.text(row["date"], row["hba1c"] + 0.05, f"{row['hba1c']}%", ha='center', va='bottom', fontsize=9, color='purple')
    ax2.set_title("HbA1c Trend")
    ax2.set_ylabel("HbA1c (%)")
    ax2.set_xlabel("Date")
    ax2.grid(True)
    ax2.legend()

    plt.tight_layout()
    filename = "combined_trend.png"
    plt.savefig(filename)
    return f"Graph saved as {filename}"

def add_hba1c_reading(date_str, hba1c_value):
    try:
        date_str = str(date_str).strip()
        parsed_date = datetime.strptime(date_str, "%d/%m/%Y").strftime("%d/%m/%Y")
        hba1c_value = float(hba1c_value)
        hba1c_str = str(int(hba1c_value)) if hba1c_value.is_integer() else str(hba1c_value)
    except (ValueError, TypeError):
        return "Invalid date or HbA1c value."

    with open("data/hba1c_readings.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([parsed_date, hba1c_str])
    return "HbA1c reading added successfully."

# --- Supplies Functions ---

def add_supply_item(item_name, quantity):
    date_str = datetime.now().strftime("%d/%m/%Y")
    with open("data/supplies.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([item_name, quantity, date_str])
    return f"Added {item_name} with {quantity} units."

def update_supply_quantity(item_name, quantity_change):
    df = pd.read_csv("data/supplies.csv")
    df.columns = df.columns.str.strip().str.lower()

    if item_name.lower() in df["item"].str.lower().values:
        index = df[df["item"].str.lower() == item_name.lower()].index[0]
        df.at[index, "quantity"] += quantity_change
        df.at[index, "last updated"] = pd.Timestamp.now().strftime("%d/%m/%Y")
        df.to_csv("data/supplies.csv", index=False)
        return f"Updated {item_name} by {quantity_change} units."
    else:
        return "Item not found."

def get_supplies():
    try:
        df = pd.read_csv("data/supplies.csv")
        df.columns = df.columns.str.strip().str.lower()
        return df
    except FileNotFoundError:
        return pd.DataFrame()

# --- Data Loaders ---

def get_glucose_df():
    try:
        df = pd.read_csv("data/glucose_readings.csv")
        df.columns = df.columns.str.strip().str.lower()
        df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y", errors="coerce")
        return df.sort_values("date")
    except FileNotFoundError:
        return pd.DataFrame()

def get_hba1c_df():
    try:
        df = pd.read_csv("data/hba1c_readings.csv")
        df.columns = df.columns.str.strip().str.lower()
        df.rename(columns={"hba1c (%)": "hba1c"}, inplace=True)
        df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y", errors="coerce")
        return df.sort_values("date")
    except FileNotFoundError:
        return pd.DataFrame()
