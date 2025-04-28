<p align="center">
  <a href="https://glucosetracker-4nhbmymvcbnhqdgpx79vjn.streamlit.app">
    <img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg" alt="Open in Streamlit">
  </a>
</p>

<p align="center">
  <a href="https://github.com/mattyhakin/glucose_tracker/releases">
    <img src="https://img.shields.io/github/v/release/mattyhakin/glucose_tracker?include_prereleases&label=release&logo=github&style=flat-square" alt="GitHub release">
  </a>
  <a href="https://github.com/mattyhakin/glucose_tracker/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/mattyhakin/glucose_tracker?style=flat-square" alt="GitHub license">
  </a>
  <img src="https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=flat-square" alt="Contributions Welcome">
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

 🔮 Future Plans

Here are some ideas for future updates to the Diabetes Tracker app:

- 📥 **Import HbA1c results via CSV** (not just manual entry)
- 📤 **Export blood glucose and HbA1c graphs as images**
- 🔒 **Optional user login** for better privacy
- 📅 **Reminders and notifications** for logging glucose and supplies
- 📈 **Daily, weekly, and monthly reports** generation
- 🖼️ **Customizable dashboard themes** (light/dark mode)
- 📱 **Mobile-friendly layout improvements** for easier use on phones and tablets
- 📊 **Add trendlines or prediction models** for glucose data

🆕 What's New

Version 1.2 (Current)

- TBC

Version 1.1 (Current)

- 🎯 Moved working data to `/data/` folder
- 📂 Added `/templates/` folder with blank CSV templates
- 🔄 Added `/examples/` folder with sample import files
- 🛠 Added `reset_data.py` script to reset working data easily
- 🚀 Improved README structure and project documentation
- 🖼️ Added custom Streamlit app favicon and page title
- 📥 Setup First Time Instructions for new users

---

 Version 1.0 (Current)

- ✅ Initial launch of Diabetes Tracker web app
- ✅ Record blood glucose readings
- ✅ Record HbA1c results
- ✅ Track diabetic supplies
- ✅ Import glucose readings via CSV
- ✅ View graphs for glucose trends and HbA1c trends
- ✅ Full deployment to Streamlit Cloud

[View full Release Notes ➡️](RELEASE_NOTES.md)

## 🛣️ Roadmap

- [x] Version 1.0 - Initial Release
- [x] Version 1.1 - Features Expansion
- [ ] [Version 1.2 - In Development 🚧](https://github.com/mattyhakin/glucose_tracker/milestone/1)

Visit the [Milestones page](https://github.com/mattyhakin/glucose_tracker/milestones) to see progress on upcoming features!

 🤝 Contributing

We welcome contributions of all kinds — bug fixes, feature suggestions, ideas!  
Feel free to open an Issue or a Pull Request anytime.

If you have suggestions for improvements, ideas for new features, or find any bugs, please feel free to:

- Fork the repository
- Create a new branch (`git checkout -b feature-YourFeatureName`)
- Make your changes
- Commit your changes (`git commit -m 'Add some feature'`)
- Push to the branch (`git push origin feature-YourFeatureName`)
- Open a Pull Request


Thanks for helping make this app better! 🎯

## 🌟 Future Ideas

- Add Dark Mode toggle for better nighttime use
- Integrate Google Sheets or OneDrive backup option
- Add email reminders for recording new readings
- Enable tracking of insulin dosages and timings
- Weekly and monthly report generation (PDF download)
- Mobile-friendly view improvements
- Set personal glucose targets and alerts
- Add basic analytics (average glucose over time, variability trends)

---

*Have more ideas? Feel free to suggest by opening an Issue!*

## 📨 Need Help or Have Ideas?

- Report a [Bug](https://github.com/mattyhakin/glucose_tracker/issues/new?template=bug_report.md)
- Suggest a [Feature](https://github.com/mattyhakin/glucose_tracker/issues/new?template=feature_request.md)
- Ask a [Question](https://github.com/mattyhakin/glucose_tracker/issues/new?template=contact_us.md)