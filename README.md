# Study-Record-Manager
# Student Record Manager

A lightweight Python command-line application built to manage student records efficiently. This project was created for the Module 2 Assignment and demonstrates core Python concepts such as file handling, input validation with regular expressions, and exception handling.

---

## 🚀 Features

- **Add Student Record**: Allows users to input Student ID, Name, and Email address.
- **Email Validation using Regex**: Uses Regular Expressions (Regex) to verify email addresses before saving them.
- **File Persistence**: Stores all student details permanently in a local `students.txt` file.
- **Read Student Records**: Fetches and neatly formats saved student records from the file.
- **Robust Exception Handling**: Prevents application crashes by catching invalid user inputs, non-integer choices, duplicate IDs, missing files, and malformed records.

---

## 🛠️ Requirements & Tech Stack

- **Language**: Python 3.x
- **Standard Libraries**: `re` (Regular Expressions)

---

## 📂 Project Structure

```text
├── main.py          # Primary Python application script
├── students.txt      # Text file generated automatically to store data
└── README.md        # Project documentation
