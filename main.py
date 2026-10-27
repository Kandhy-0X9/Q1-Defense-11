import sqlite3

data_to_insert = []

def add_students(students_data):
    # 1. Connect to a database file
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    
    # 2. Create the table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            grade TEXT
        );
    ''')
    
    # 3. Insert the data safely using executemany
    cursor.executemany('''
        INSERT INTO students (name, age, grade) 
        VALUES (?, ?, ?);
    ''', students_data)
    
    # 4. Commit the changes and close the connection
    conn.commit()
    print("Database created and data inserted successfully!")

# Collect input from the user
def add_student():
    name = input("What is your name: ").strip().title()
    age = int(input("What is your age: "))
    grade = input("What is your grade (A, B, C...): ").strip().upper()

    data_to_insert.append((name, age, grade))

def menu():
    choice = input("What do you want to do")



print("---Student Database---")