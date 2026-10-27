
import sqlite3
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def connect_db():# connects to the db every time its called
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            grade TEXT
        )
    """)
    conn.commit()
    return conn


def add_student():
    clear_screen()
    name = input("What is your name: ").strip().title()
    if not name:
        print("Name cannot be empty")
        return
    try:
        age = int(input("What is your age: "))
        if not 1 <= age <=120:
            print("Age cannot be less than 1 or greater than 120.")
            return
    except ValueError:
        print("Please enter a valid number for age.")
        return
    grade = input("What is your grade (A, B, C...): ").strip().upper()
    if grade not in ("A", "B", "C", "D", "F"):
        print("Please enter a valid grade.")
        return
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO students (name, age, grade)
        VALUES (?, ?, ?)
    """, (name, age, grade))
    conn.commit()
    conn.close()
    print("Student added successfully!")


def display_students():
    clear_screen()
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    if students:
        for student in students:
            print(student)
    else:
        print("No students found.")
    conn.close()


def update_grade():
    clear_screen()
    student_id = input("Enter the student ID: ").strip()
    new_grade = input("Enter the new grade: ").strip().upper()
    try:
        student_id = int(student_id)
    except ValueError:
        print("Please enter a valid student ID.")
        return
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE students
        SET grade = ?
        WHERE id = ?
    """, (new_grade, student_id))
    conn.commit()
    if cursor.rowcount > 0:
        print("Grade updated successfully!")
    else:
        print("Student ID not found.")
    conn.close()


def search_name():
    clear_screen()
    name = input("Enter the student's name: ").strip()
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM students
        WHERE name LIKE ?
    """, (f"%{name}%",))
    students = cursor.fetchall()
    if students:
        for student in students:
            print(student)
    else:
        print("No matching students found.")
    conn.close()


def show_by_grade():
    clear_screen()
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT grade, COUNT(*)
        FROM students
        GROUP BY grade
        ORDER BY grade
    """)
    results = cursor.fetchall()
    if results:
        for grade, count in results:
            print(f"Grade {grade}: {count} student(s)")
    else:
        print("No students found.")
    conn.close()


def delete_student():
    clear_screen()
    try:
        student_id = int(input("Enter the student ID to delete: "))
    except ValueError:
        print("Please enter a valid student ID.")
        return
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM students
        WHERE id = ?
    """, (student_id,))
    conn.commit()
    if cursor.rowcount > 0:
        print("Student deleted successfully!")
    else:
        print("Student ID not found.")
    conn.close()
    

def main():
    clear_screen()
    while True:
        choice = input(
            "\nOptions:\n"
            "  add     => Add a student\n"
            "  display => Display all students\n"
            "  update  => Update a student's grade\n"
            "  search  => Search for a student by name\n"
            "  show    => Count students in each grade\n"
            "  delete  => Delete a student\n"
            "  exit    => Exit the program\n"
            "What is your choice: "
        ).strip().lower()

        if choice == "add":
            add_student()
        elif choice == "display":
            display_students()
        elif choice == "update":
            update_grade()
        elif choice == "search":
            search_name()
        elif choice == "show":
            show_by_grade()
        elif choice == "delete":
            delete_student()
        elif choice == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
