#My glucose reading tracker
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

# Example usage:
if __name__ == "__main__":
    # Manual test: replace with your actual values or input()
    import_glucose_readings("import_me.csv")