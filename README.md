# Expence-Tracker

A lightweight, console-based **Python application** designed to track daily expenses without any external dependencies. It allows users to quickly add expenses with descriptions, view their tracking history, and cleanly exit the program.

## 🚀 Features

* **Interactive Menu:** Simple console interface for easy navigation.
* **Add Expenses:** Log numerical expense amounts along with custom descriptions.
* **View History:** Review all recorded transactions with dynamic, numbered formatting.
* **Zero Dependencies:** Runs entirely on standard Python 3 libraries.

---

## 🛠️ Code Structure Overview

The application stores data in a dynamic list named `expenses` and runs inside a `while True` loop to process the following choices:

1. **Choice 1 (Add Expense):** 
   * Captures the expense amount as a floating-point number.
   * Prompts for a short description.
   * Appends a dictionary containing `{"amount": amount, "description": description}` into the local list.
2. **Choice 2 (View Expenses):** 
   * Checks if any items are recorded.
   * Loops through and prints all entries in a clear `ID. Amount: [X], Description: [Y]` format.
3. **Choice 3 (Exit):** 
   * Displays a goodbye message and breaks the loop to terminate the program safely.

---

## 📋 Prerequisites

To run this project, you only need **Python 3.x** installed on your system. No extra packages or pip installations are required.

---

## 💻 How to Run

1. Make sure the code is saved in a file named `expense_tracker.py`.
2. Open your terminal or command prompt in the same folder where the file is located.
3. Execute the script by running:

```bash
python expense_tracker.py
```

---

## 📝 Example Terminal Preview

```text
Welcome to Expense Tracker
1. Add Expense
2. View Expenses
3. Exit
Enter your choice: 1

Enter expense amount: 15.50
Enter expense description: Lunch at the cafeteria
Expense added successfully!

Welcome to Expense Tracker
1. Add Expense
2. View Expenses
3. Exit
Enter your choice: 2

1. Amount: 15.5, Description: Lunch at the cafeteria
```
