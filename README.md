<p align="center">
  <a href="https://glucosetracker-4nhbmymvcbnhqdgpx79vjn.streamlit.app">
    <img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg" alt="Open in Streamlit">
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Version-1.0-brightgreen" alt="version">
</p>

# Diabetes Tracker Web App

A simple and personal web app to track:

- Blood glucose readings
- HbA1c lab results
- Diabetic supplies (e.g., insulin, test strips)

Built using **Python**, **Streamlit**, **Pandas**, and **Matplotlib**.

---

## 🚀 Live App

[Click here to view the live app!](https://glucosetracker-4nhbmymvcbnhqdgpx79vjn.streamlit.app)

---

## 📋 Features

- Add new glucose readings manually
- Add HbA1c lab results
- Import glucose readings from CSV files
- View graphs for glucose trends and HbA1c
- Manage diabetic supplies inventory
- Download and upload data easily
- An example `import_me.csv` file is included in the `examples/` folder.
- You can use it to practice importing glucose readings into the app.

---

## 🛠 Tech Stack

- Streamlit
- Pandas
- Matplotlib
- GitHub

---

## 📂 Folder Structure
```
glucose_tracker/
├── data/
│   ├── glucose_readings.csv      # Your actual working glucose data
│   ├── hba1c_readings.csv         # Your actual working HbA1c data
│   ├── supplies.csv               # Your actual working supplies data
├── templates/
│   ├── glucose_readings_template.csv   # Blank glucose readings template
│   ├── hba1c_readings_template.csv      # Blank HbA1c template
│   ├── supplies_template.csv           # Blank supplies template
├── examples/
│   ├── import_me.csv              # Example file for testing imports (optional)
├── .streamlit/
│   └── config.toml                 # App configuration (page title, favicon, etc.)
├── utils.py                        # All backend functions
├── streamlit_app.py                 # Streamlit front-end app
├── requirements.txt                 # Python package dependencies
├── reset_data.py                    # NEW! Resets data from templates
└── README.md                        # Documentation for project
```

---

## 📥 First Setup

When first cloning or using the app:

- The real working data is located in the `data/` folder.
- If you prefer to start fresh, copy the blank templates from the `templates/` folder into the `data/` folder.
- Templates include:
  - glucose_readings_template.csv
  - hba1c_readings_template.csv
  - supplies_template.csv

✅ This ensures the app has the correct structure even if no readings have been entered yet.

---

## 👨‍💻 About

This project was built to help manage diabetes more easily — track important readings, monitor trends, and keep your supplies organized, all from one simple app.

---

## 🔄 Resetting Data

To reset your app's data back to a clean state (blank templates):

1. Open your terminal inside the project folder.
2. Run:

```bash
python reset_data.py

*Built with love using Python and Streamlit.*

## 🔮 Future Plans

Here are some ideas for future updates to the Diabetes Tracker app:

- 📥 **Import HbA1c results via CSV** (not just manual entry)
- 📤 **Export blood glucose and HbA1c graphs as images**
- 🔒 **Optional user login** for better privacy
- 📅 **Reminders and notifications** for logging glucose and supplies
- 📈 **Daily, weekly, and monthly reports** generation
- 🖼️ **Customizable dashboard themes** (light/dark mode)
- 📱 **Mobile-friendly layout improvements** for easier use on phones and tablets
- 📊 **Add trendlines or prediction models** for glucose data