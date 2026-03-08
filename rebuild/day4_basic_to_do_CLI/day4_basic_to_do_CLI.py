#sys
#os
#def (functions)
#return
#with open
#if __name__ == "__main__":
#    main()

import sys
import os

TASK_FILE = "tasks.txt"


def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []

    with open(TASK_FILE, "r") as f:
        return [task.strip() for task in f.readlines()]


def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")


def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {task}")


def list_tasks():
    tasks = load_tasks()

    if not tasks:
        print("No tasks found.")
        return

    print("Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")


def delete_task(index):
    tasks = load_tasks()

    if index < 1 or index > len(tasks):
        print("Invalid task number.")
        return

    removed = tasks.pop(index - 1)
    save_tasks(tasks)
    print(f"Deleted task: {removed}")


def main():
    if len(sys.argv) < 2:
        print("Commands:")
        print(" add \"task\"")
        print(" list")
        print(" delete <number>")
        return

    command = sys.argv[1]

    if command == "add":
        task = sys.argv[2]
        add_task(task)

    elif command == "list":
        list_tasks()

    elif command == "delete":
        index = int(sys.argv[2])
        delete_task(index)

    else:
        print("Unknown command")


if __name__ == "__main__":
    main()