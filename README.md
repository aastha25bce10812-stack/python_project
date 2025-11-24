# python_project
 Student Result Management System

## Overview
This is a simple console-based Python application designed to manage student academic results. It allows users to add new student records, view all existing records, and search for specific students using their roll numbers. All student data is stored persistently in a CSV file named `students.csv`.

## Features
*   **Add Student Records**: Input student's Roll Number, Name, and marks for three subjects. The system automatically calculates total marks, percentage, and assigns a grade.
*   **View All Students**: Display a list of all recorded students along with their details.
*   **Search Student**: Find a student's record by entering their unique Roll Number.
*   **Data Persistence**: All student data is saved and loaded from a CSV file, ensuring data is not lost when the application closes.

## Technologies/Tools Used
*   **Python 3**: The core programming language.
*   **CSV Module**: Python's built-in module for handling CSV (Comma Separated Values) files for data storage.

## Steps to Install & Run the Project
1.  **Save the Code**: Copy the provided Python code into a file named `student_management.py` (or any other `.py` extension).
2.  **Run from Terminal**: Open your terminal or command prompt, navigate to the directory where you saved the file, and execute the following command:
    ```bash
    python student_management.py
    ```
3.  **First Run**: Upon the first execution, a `students.csv` file will be automatically created with a header row.

## Instructions for Testing
Once the application is running, you can interact with it via the console menu:

1.  **Add Students**: Select option `1` from the main menu. Enter sample Roll Numbers, Names, and Marks for 3 subjects. Add a few students to populate the system.
2.  **View All Students**: Select option `2`. Verify that all the students you added are displayed correctly, including their calculated total, percentage, and grade.
3.  **Search Student**: Select option `3`. Enter the Roll Number of a student you previously added. Confirm that their record is displayed. Also, try searching for a non-existent Roll Number to see the "Student not found!" message.
4.  **Exit**: Select option `4` to gracefully exit the application.

## Screenshots
<img width="1918" height="964" alt="Screenshot 2025-11-24 224940" src="https://github.com/user-attachments/assets/0d53b92c-4908-4f66-a40d-2a358b86b856" />
<img width="1916" height="953" alt="Screenshot 2025-11-24 225116" src="https://github.com/user-attachments/assets/a6a683a3-acb0-45b5-8758-a52ce6d9a99e" />
<img width="1919" height="958" alt="Screenshot 2025-11-24 225140" src="https://github.com/user-attachments/assets/92a5205b-5384-4f6b-8cdb-e77719ee0961" />
