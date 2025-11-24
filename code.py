import csv

FILE_NAME = "students.csv"

# Create the file with header if not present
def initialize_file():
    try:
        with open(FILE_NAME, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Roll No", "Name", "Marks1", "Marks2", "Marks3", "Total", "Percentage", "Grade"])
    except FileExistsError:
        pass

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    m1 = float(input("Enter Marks 1 (out of 100): "))
    m2 = float(input("Enter Marks 2 (out of 100): "))
    m3 = float(input("Enter Marks 3 (out of 100): "))

    total = m1 + m2 + m3
    #marks percentage
    percentage = total / 3
    #calling calculate_grade to fid grade of the student
    grade = calculate_grade(percentage)

    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, m1, m2, m3, total, percentage, grade])

    print("Student record added successfully!\n")

def view_all_students():
    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
        print()
    except FileNotFoundError:
        print("No student records found!\n")

def search_student():
    roll = input("Enter Roll Number to search: ")
    found = False

    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == roll:
                    print("Student Found:")
                    print(row)
                    found = True
                    break

        if not found:
            print("Student not found!\n")

    except FileNotFoundError:
        print("No records available!\n")

def main():
    initialize_file()

    while True:
        print("------ Student Result Management ------")
        print("1. Add Student Result")
        print("2. View All Students")
        print("3. Search Student by Roll No")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_all_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            print("Thank you! Exiting...")
            break
        else:
            print("Invalid option! Try again.\n")


if __name__ == "__main__":
    main()
