# 📌 Study Reminder App

A specialized desktop automation tool designed to help students and professionals stick to their schedules. This application reads task data from an Excel file and triggers real-time desktop notifications and automated browser actions based on a predefined "Weekend Plan."

---

## ✨ Features

* **Excel Integration:** Seamlessly pulls schedule data (Day, Time, Task, Duration, Resource) from a local `.xlsx` file.
* **Real-time Notifications:** Uses system-level alerts to notify you exactly when a task starts.
* **Auto-Resource Launcher:** Automatically opens study links, meeting URLs, or digital resources in your default web browser at the scheduled time.
* **Background Processing:** Operates using multi-threading, allowing the reminder engine to run without freezing the GUI.
* **Daily Agenda Viewer:** Quick-access button to view all tasks scheduled for the current day in a scrollable window.

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Data Handling:** `pandas`, `openpyxl`
* **GUI Framework:** `Tkinter`
* **Automation Tools:** `webbrowser`, `plyer` (for notifications)
* **Concurrency:** `threading`

---

## 📁 Folder Structure

```text
study-reminder-app/
├── main.py
├── weekend_plan.xlsx
└── README.md

```

---

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/FAHAD-ALI-github/study-reminder-app

# Navigate into the project directory
cd study-reminder-app

# Install necessary dependencies
pip install pandas openpyxl plyer

# Ensure your weekend_plan.xlsx is in the root folder with columns:
# [Day, Time Slot, Subject / Task, Duration, Type, Resource]

# Run the application
python main.py

```

---

## 🌐 Live Demo

[🔗 Live Site](https://your-live-demo-link.com)

---

## 👤 Author

**Fahad Ali** GitHub: [@FAHAD-ALI-github](https://github.com/FAHAD-ALI-github)

LinkedIn: [fahadali1078](https://www.linkedin.com/in/fahadali1078/)
