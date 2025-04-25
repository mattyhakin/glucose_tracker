#My glucose reading tracker
from utils import (
    add_glucose_reading,
    add_hba1c_reading,
    import_glucose_readings,
    search_glucose_readings,
    plot_glucose_trend,
    plot_glucose_with_rolling_avg,
    plot_hba1c_trend,
    plot_combined_trend
)

def main_menu():
    while True:
        print("\n--- Glucose Tracker Menu ---")
        print("1. Add a new glucose reading")
        print("2. Add a new HbA1c reading")
        print("3. Import readings from a CSV")
        print("4. Search readings")
        print("5. View glucose level graph")
        print("6. View graph with rolling average")
        print("7. View HbA1c trend graph")
        print("8. View combined glucose & HbA1c trend")
        print("9. Exit")
        
        choice = input("Choose an option (1-9): ").strip()

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
            date = input("Enter date (DD/MM/YYYY): ")
            value = input("Enter HbA1c value (%): ")
            add_hba1c_reading(date, value)

        elif choice == "3":
            filename = input("Enter the import file name (e.g. import_me.csv): ")
            import_glucose_readings(filename)

        elif choice == "4":
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

        elif choice == "5":
            plot_glucose_trend()

        elif choice == "6":
            plot_glucose_with_rolling_avg()
        
        elif choice == "7":
            plot_hba1c_trend()
        
        elif choice == "8":
            plot_combined_trend()

        elif choice == "9":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

# Example usage:
if __name__ == "__main__":
    main_menu()