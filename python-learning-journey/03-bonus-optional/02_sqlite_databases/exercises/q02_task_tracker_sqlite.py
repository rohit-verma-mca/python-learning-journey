"""
Question:
Create a tasks table (id, task, done). Write functions to add a task,
mark a task as done (update), view all tasks, and delete a completed
task.

Topic     : SQLite, Databases
Source    : Suggested exercise
Difficulty: Medium
"""

import sqlite3

DB_FILE = "tasks.db"


def create_table():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            done INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()


def add_task(task):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task, done) VALUES (?, 0)", (task,))
    conn.commit()
    conn.close()
    print(f"Added task: {task}")


def mark_task_done(task_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    print(f"Marked task {task_id} as done")


def view_all_tasks():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    conn.close()

    print("All tasks:")
    for row in rows:
        status = "Done" if row[2] == 1 else "Pending"
        print(f"{row[0]}. {row[1]} - {status}")
    return rows


def delete_task(task_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    print(f"Deleted task {task_id}")


if __name__ == "__main__":
    create_table()
    add_task("Finish SQLite exercise")
    add_task("Push today's code")
    add_task("Revise regex notes")

    view_all_tasks()

    mark_task_done(1)
    print("\nAfter marking task 1 done:")
    view_all_tasks()

    delete_task(1)
    print("\nAfter deleting task 1:")
    view_all_tasks()