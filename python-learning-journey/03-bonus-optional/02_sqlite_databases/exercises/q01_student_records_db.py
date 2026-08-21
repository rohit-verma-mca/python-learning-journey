"""
Question:
Create a database with a students table (name, age, marks). Write
functions to add a student, view all students, and find a student
by name.

Topic     : SQLite, Databases
Source    : Suggested exercise
Difficulty: Medium
"""

import sqlite3

DB_FILE = "students.db"


def create_table():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            marks REAL
        )
    """)
    conn.commit()
    conn.close()


def add_student(name, age, marks):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, marks) VALUES (?, ?, ?)", (name, age, marks))
    conn.commit()
    conn.close()
    print(f"Added student: {name}")


def view_all_students():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()

    print("All students:")
    for row in rows:
        print(row)
    return rows


def find_student(name):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
    result = cursor.fetchone()
    conn.close()

    if result:
        print(f"Found: {result}")
    else:
        print(f"No student found with name '{name}'")
    return result


if __name__ == "__main__":
    create_table()
    add_student("Rahul", 22, 85.5)
    add_student("Priya", 21, 91.0)

    view_all_students()
    find_student("Rahul")
    find_student("Someone")