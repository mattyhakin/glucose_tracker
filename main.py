#My glucose reading tracker
from utils import (
    add_glucose_reading,
    import_glucose_readings,
    search_glucose_readings
)

def main_menu():
    while True:
        print("\n--- Glucose Tracker Menu ---")
        print("1. Add a new glucose reading")
        print("2. Import readings from a CSV")
        print("3. Search readings")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            date = input("Enter date (DD/MM/YYYY): ")
            time = input("Enter time (HH:MM or -): ")
            try:
                level = float(input("Enter glucose level: "))
            except ValueError:
                print("Invalid glucose level.")
                continue
            notes = input("Enter notes (or -): ")
            add_glucose_reading(date, time, level, notes)

        elif choice == "2":
            filename = input("Enter the import file name (e.g. import_me.csv): ")
            import_glucose_readings(filename)

        elif choice == "3":
            print("\nSearch by:")
            print("1. Date")
            print("2. Level above")
            print("3. Level below")
            print("4. Notes")
            sub_choice = input("Choose search type (1-4): ").strip()

            if sub_choice == "1":
                value = input("Enter date (DD/MM/YYYY): ")
                search_glucose_readings("date", value)
            elif sub_choice == "2":
                value = input("Enter minimum level: ")
                search_glucose_readings("level_above", value)
            elif sub_choice == "3":
                value = input("Enter maximum level: ")
                search_glucose_readings("level_below", value)
            elif sub_choice == "4":
                value = input("Enter keyword for notes: ")
                search_glucose_readings("note", value)
            else:
                print("Invalid option.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

# Example usage:
if __name__ == "__main__":
    main_menu()