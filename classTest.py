import sqlite3
import os

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

grades = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"]

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    def save_to_db(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO students (name, age, grade)
            VALUES (?, ?, ?)
        """, (self.name, self.age, self.grade))
        conn.commit()
        conn.close()


def add_student(name, age, grade):
    student = Student(name, age, grade)
    student.save_to_db()
    return student
