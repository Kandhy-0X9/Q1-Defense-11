import sqlite3

# 1. Connect to a database file (it will be created if it doesn't exist)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# 2. Create the table (Fixed the "INTERGER" typos)
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
);
""")

# 3. Insert the data
students_data = []

# Use executemany to safely insert multiple rows at once
cursor.executemany("""
INSERT INTO students (name, age, grade)
VALUES ('Alice', 18, 'A');

INSERT INTO students (name, age, grade)
VALUES ('Bob', 20, 'B');

INSERT INTO students (name, age, grade)
VALUES ('Charlie', 19, 'A');
""", students_data)


# 4. Commit the changes and close the connection
conn.commit()
conn.close()

print("Database created and data inserted successfully!")
