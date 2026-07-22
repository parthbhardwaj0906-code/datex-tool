# Datex 📊

**Datex** is an automated data integrity and cleaning application built with Flask and Pandas. It processes raw datasets to identify structural irregularities, handle missing values, and address numerical outliers—delivering clean, analysis-ready CSV files.

---

## ✨ Features

* **In-Memory Dataset Processing:** Cleans and formats datasets on the fly without saving raw files to disk.
* **Automated Data Cleaning:** Automatically strips whitespace, drops duplicate entries, and manages missing values and outliers.
* **Two-Step Download & Terms Flow:** Clear agreement confirmation process before serving cleaned output files.
* **Streamlined UX:** Responsive, dark-themed UI built for fast interaction.

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Data Processing:** Pandas, NumPy
* **Frontend:** HTML5, CSS3, JavaScript (Vanilla)

---

## 📁 Project Structure
```text
├── application.py      # Main Flask application & route handlers
├── cleaner.py          # Data processing logic (missing values, outliers, formatting)
├── templates/
│   ├── home.html       # Home
|   ├── choice.html     # Data upload page and asks for choices regarding the data.
│   ├── results.html    # Summary of detected irregularities
│   ├── download.html   # Agreement notice and download trigger
│   └── thankyou.html   # Download confirmation and navigation
└── requirements.txt    # Python dependencies
```
