
# CS492 Mosques Management System

This is a simple desktop application developed using Python and Tkinter for managing mosques' data. It is a course project for CS492.

## 🕌 Features

- Add new mosques with details.
- Edit and delete existing mosque records.
- View a list of all mosques.
- Data persistence using SQLite (`mosques.db`).
- Simple GUI built with Tkinter.

## 🛠️ Technologies Used

- Python 3.x
- Tkinter (built-in GUI library)
- SQLite (for local database storage)

## 📦 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/ehrg1/CS492-mosques-management.git
   cd CS492-mosques-management
   ```

2. **Run the application**

   Make sure Python 3 is installed, then run:

   ```bash
   python main.py
   ```

> No additional dependencies are required as the project uses standard Python libraries.

## 🗂 Project Structure

```
CS492-mosques-management/
│
├── main.py          # Main script to launch the GUI
├── mosque.py        # Logic for managing mosque data
├── mosques.db       # SQLite database file
├── icon.png         # App icon
└── __pycache__/     # Auto-generated cache by Python
```

## ✅ Usage

- Click **Add** to insert a new mosque record.
- Select a mosque from the list and click **Edit** or **Delete**.
- All data is saved automatically to `mosques.db`.


Developed by [@ehrg1](https://github.com/ehrg1) for CS492.
