import re

FILE_NAME = "students.txt"


def validate_email(email):
    """Validate email format using Regex."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email.strip()) is not None


def student_exists(student_id):
    """Check if student ID already exists in the file."""
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if parts and parts[0] == str(student_id):
                    return True
    except FileNotFoundError:
        return False
    return False


def add_student():
    """Add a new student with input validation and exception handling."""
    try:
        student_id_input = input("Enter Student ID: ").strip()

        # Exception Handling: Validate positive integer for ID
        if not student_id_input.isdigit():
            raise ValueError("Student ID must be a positive number.")

        student_id = int(student_id_input)

        if student_exists(student_id):
            raise ValueError(f"Student ID {student_id} already exists.")

        name = input("Enter Student Name: ").strip()
        email = input("Enter Student Email: ").strip()

        # Exception Handling: Validate empty name
        if not name:
            raise ValueError("Name cannot be empty.")

        # Regex Validation for Email
        if not validate_email(email):
            raise ValueError("Invalid email format.")

        # Save Data to File
        with open(FILE_NAME, "a") as file:
            file.write(f"{student_id},{name},{email}\n")

        print("Student added successfully!")

    except ValueError as e:
        print("Error:", e)


def read_students():
    """Read and display student records from the file."""
    try:
        # Read Data from File
        with open(FILE_NAME, "r") as file:
            data = file.readlines()

        records = [line.strip() for line in data if line.strip()]

        if not records:
            print("No student records found.")
            return

        print("\nStudent Records")
        print("--------------------")

        for record in records:
            parts = record.split(",")

            if len(parts) != 3:
                continue  # Skip malformed lines

            student_id, name, email = parts

            print("ID:", student_id)
            print("Name:", name)
            print("Email:", email)
            print("--------------------")

    except FileNotFoundError:
        print("No student data file found.")


def main():
    while True:
        print("\n===== Student Record Manager =====")
        print("1. Add Student")
        print("2. Read Student Data")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_student()
            elif choice == 2:
                read_students()
            elif choice == 3:
                print("Thank you!")
                break
            else:
                print("Please enter a number between 1 and 3.")

        except ValueError:
            print("Invalid input! Please enter a number.")


if __name__ == "__main__":
    main()