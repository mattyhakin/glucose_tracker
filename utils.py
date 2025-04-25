import pandas as pd 
import csv
from datetime import datetime

def add_glucose_reading(date, time, level, notes):
    with open("glucose_readings.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, time, level, notes])
    print("Reading added successfully.")

def import_glucose_readings(import_file):
    try:
        df = pd.read_csv(import_file)
    except FileNotFoundError:
        print("Import file not found.")
        return

    rows_to_add = []
    for _, row in df.iterrows():
        try:
            date = datetime.strptime(str(row["Date"]).strip(), "%d/%m/%Y").strftime("%d/%m/%Y")
            time = str(row["Time"]).strip() if not pd.isna(row["Time"]) else "-"
            level = float(row["Glucose Level"])
            notes = str(row["Notes"]).strip() if not pd.isna(row["Notes"]) else "-"
            rows_to_add.append([date, time, level, notes])
        except Exception as e:
            print(f"Skipping row due to error: {e}")
            continue

    # Write to your main file
    with open("glucose_readings.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows_to_add)

    print(f"Imported {len(rows_to_add)} rows successfully.")

def search_glucose_readings(by="date", value=None):
    try:
        df = pd.read_csv("glucose_readings.csv")
        df.columns = df.columns.str.strip().str.lower()  # Make all column names lowercase

        if "date" not in df.columns or "level" not in df.columns:
            print("CSV missing required columns.")
            return

        df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y", errors="coerce")

    except FileNotFoundError:
        print("No readings found.")
        return

    if by == "date":
        try:
            target_date = datetime.strptime(value, "%d/%m/%Y").date()
            result = df[df["date"].dt.date == target_date]
        except Exception as e:
            print(f"Invalid date format: {e}")
            return

    elif by == "level_above":
        result = df[df["level"] > float(value)]

    elif by == "level_below":
        result = df[df["level"] < float(value)]

    elif by == "note":
        result = df[df["notes"].str.contains(str(value), case=False, na=False)]

    else:
        print("Invalid search type.")
        return

    if result.empty:
        print("No matching records found.")
    else:
        print(result)

import matplotlib.pyplot as plt

def plot_glucose_trend():
    try:
        df = pd.read_csv("glucose_readings.csv")
        df.columns = df.columns.str.strip().str.lower()
        df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y", errors="coerce")
    except FileNotFoundError:
        print("No readings found.")
        return

    if df.empty:
        print("No data to plot.")
        return

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
    print(f"Graph saved as {filename}. You can download or open it from the file panel.")

def plot_glucose_with_rolling_avg():
    try:
        df = pd.read_csv("glucose_readings.csv")
        df.columns = df.columns.str.strip().str.lower()
        df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y", errors="coerce")
    except FileNotFoundError:
        print("No readings found.")
        return

    if df.empty:
        print("No data to plot.")
        return

    df = df.sort_values("date")
    df = df.dropna(subset=["level"])

    # Calculate rolling averages
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
    print(f"Saved graph as {filename}")

def plot_hba1c_trend():
    try:
        df = pd.read_csv("hba1c_readings.csv")
        df.columns = df.columns.str.strip().str.lower()
        df.rename(columns={"hba1c (%)": "hba1c"}, inplace=True)
        df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y", errors="coerce")
    except FileNotFoundError:
        print("No HbA1c file found.")
        return

    if df.empty or "hba1c" not in df.columns:
        print("No valid HbA1c data to plot.")
        return

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
    print(f"Saved HbA1c graph as {filename}")

def plot_combined_trend():
    try:
        # Load glucose data
        glucose_df = pd.read_csv("glucose_readings.csv")
        glucose_df.columns = glucose_df.columns.str.strip().str.lower()
        glucose_df["date"] = pd.to_datetime(glucose_df["date"], format="%d/%m/%Y", errors="coerce")
        glucose_df = glucose_df.sort_values("date")
        glucose_df = glucose_df.dropna(subset=["level"])
        glucose_df["7_day_avg"] = glucose_df["level"].rolling(window=7).mean()
        glucose_df["30_day_avg"] = glucose_df["level"].rolling(window=30).mean()

        # Load HbA1c data
        hba1c_df = pd.read_csv("hba1c_readings.csv")
        hba1c_df.columns = hba1c_df.columns.str.strip().str.lower()
        hba1c_df.rename(columns={"hba1c (%)": "hba1c"}, inplace=True)
        hba1c_df["date"] = pd.to_datetime(hba1c_df["date"], format="%d/%m/%Y", errors="coerce")
        hba1c_df = hba1c_df.sort_values("date")
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    if glucose_df.empty or hba1c_df.empty:
        print("Not enough data to plot combined view.")
        return

    # Plot setup
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

    # Glucose trend plot
    ax1.plot(glucose_df["date"], glucose_df["level"], label="Glucose Level", marker='o', alpha=0.6)
    ax1.plot(glucose_df["date"], glucose_df["7_day_avg"], label="7-Day Avg", color='red', linewidth=2)
    ax1.plot(glucose_df["date"], glucose_df["30_day_avg"], label="30-Day Avg", color='green', linewidth=2)
    ax1.set_title("Glucose Levels and Rolling Averages")
    ax1.set_ylabel("Glucose Level")
    ax1.grid(True)
    ax1.legend()

    # HbA1c plot
    ax2.plot(hba1c_df["date"], hba1c_df["hba1c"], label="HbA1c (%)", marker='o', color='purple', linewidth=2)
    ax2.set_title("HbA1c Trend")
    ax2.set_ylabel("HbA1c (%)")
    ax2.set_xlabel("Date")
    ax2.grid(True)
    ax2.legend()

    plt.tight_layout()
    filename = "combined_trend.png"
    plt.savefig(filename)
    print(f"Saved combined graph as {filename}")

def add_hba1c_reading(date_str, hba1c_value):
    try:
        date_str = str(date_str).strip()
        parsed_date = datetime.strptime(date_str, "%d/%m/%Y").strftime("%d/%m/%Y")
        hba1c_value = float(hba1c_value)
    except (ValueError, TypeError):
        print("Invalid date or HbA1c value.")
        return

    with open("hba1c_readings.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([parsed_date, hba1c_value])
    print("HbA1c reading added successfully.")