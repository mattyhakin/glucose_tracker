import shutil
import os

# Define the folders
TEMPLATE_FOLDER = "templates"
DATA_FOLDER = "data"

# List of files to reset
files_to_reset = [
    ("glucose_readings_template.csv", "glucose_readings.csv"),
    ("hba1c_readings_template.csv", "hba1c_readings.csv"),
    ("supplies_template.csv", "supplies.csv"),
]

def reset_data():
    for template_file, target_file in files_to_reset:
        template_path = os.path.join(TEMPLATE_FOLDER, template_file)
        target_path = os.path.join(DATA_FOLDER, target_file)
        shutil.copy(template_path, target_path)
    return "All data files have been reset to blank templates!"

if __name__ == "__main__":
    print(reset_data())