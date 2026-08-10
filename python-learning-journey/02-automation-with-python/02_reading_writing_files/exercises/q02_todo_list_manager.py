"""
Question:
Write a program that lets you add a task (appends it to a todo.txt file),
view all tasks (reads and prints the file), and clear all tasks
(overwrites the file empty).

Topic     : File I/O
Source    : Suggested exercise
Difficulty: Easy
"""

TODO_FILE = "todo.txt"


def add_task(task):
    with open(TODO_FILE, "a") as f:
        f.write(task + "\n")


def view_tasks():
    try:
        with open(TODO_FILE, "r") as f:
            tasks = f.readlines()
    except FileNotFoundError:
        print("No tasks yet.")
        return

    if not tasks:
        print("No tasks yet.")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task.strip()}")


def clear_tasks():
    with open(TODO_FILE, "w") as f:
        pass
    print("All tasks cleared.")


if __name__ == "__main__":
    add_task("Finish regex chapter")
    add_task("Push today's exercises")
    add_task("Revise loops notes")

    print("Current tasks:")
    view_tasks()

    clear_tasks()
    print("\nAfter clearing:")
    view_tasks()
    