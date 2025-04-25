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