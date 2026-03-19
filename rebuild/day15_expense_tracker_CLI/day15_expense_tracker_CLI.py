import os

expenses = []
FILE_NAME = "expenses.txt"


# Load expenses from file
def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, amount = line.strip().split(",")
                expenses.append((name, float(amount)))


# Save expenses to file
def save_expenses():
    with open(FILE_NAME, "w") as file:
        for name, amount in expenses:
            file.write(f"{name},{amount}\n")


# Show menu
def show_menu():
    print("\n==== Expense Tracker ====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Delete Expense")
    print("5. Exit")


# Add expense
def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))

    expenses.append((name, amount))
    save_expenses()

    print("Expense added successfully.")


# View expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    print("\n--- Your Expenses ---")
    for i, (name, amount) in enumerate(expenses, start=1):
        print(f"{i}. {name} - ₱{amount}")


# Show total spending
def show_total():
    total = sum(amount for _, amount in expenses)
    print(f"\nTotal Spending: ₱{total}")


# Delete expense
def delete_expense():
    view_expenses()

    if not expenses:
        return

    try:
        index = int(input("Enter expense number to delete: ")) - 1

        if 0 <= index < len(expenses):
            removed = expenses.pop(index)
            save_expenses()
            print(f"Deleted: {removed[0]} - ₱{removed[1]}")
        else:
            print("Invalid number.")

    except ValueError:
        print("Please enter a valid number.")


# Main program
def main():
    load_expenses()

    while True:
        show_menu()

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            show_total()

        elif choice == "4":
            delete_expense()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()