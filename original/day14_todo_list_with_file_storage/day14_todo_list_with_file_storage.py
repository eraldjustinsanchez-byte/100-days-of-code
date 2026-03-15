tasks = []

try:
    with open("tasks.txt", "r") as file:
        tasks = file.read().splitlines()
except FileNotFoundError:
    pass


def show_menu():
    print("\nTodo List")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")


def view_tasks():
    if not tasks:
        print("No tasks found.")
        return

    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")


def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks()


def delete_task():
    view_tasks()

    try:
        task_num = int(input("Enter task number to delete: "))
        tasks.pop(task_num - 1)
        save_tasks()
    except:
        print("Invalid task number.")


def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


while True:

    show_menu()

    choice = input("Choose an option: ")

    if choice == "1":
        view_tasks()

    elif choice == "2":
        add_task()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")