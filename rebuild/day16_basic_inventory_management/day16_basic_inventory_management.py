import os

inventory = []
FILE_NAME = "inventory.txt"


# Load inventory from file
def load_inventory():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, quantity = line.strip().split(",")
                inventory.append((name, int(quantity)))


# Save inventory to file
def save_inventory():
    with open(FILE_NAME, "w") as file:
        for name, quantity in inventory:
            file.write(f"{name},{quantity}\n")


# Show menu
def show_menu():
    print("\n==== Inventory Management ====")
    print("1. Add Item")
    print("2. View Inventory")
    print("3. Update Quantity")
    print("4. Delete Item")
    print("5. Exit")


# Add item
def add_item():
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))

    inventory.append((name, quantity))
    save_inventory()

    print("Item added successfully.")


# View inventory
def view_inventory():
    if not inventory:
        print("Inventory is empty.")
        return

    print("\n--- Inventory List ---")
    for i, (name, quantity) in enumerate(inventory, start=1):
        print(f"{i}. {name} - Qty: {quantity}")


# Update quantity
def update_item():
    view_inventory()

    if not inventory:
        return

    try:
        index = int(input("Enter item number to update: ")) - 1

        if 0 <= index < len(inventory):
            name, _ = inventory[index]
            new_quantity = int(input("Enter new quantity: "))

            inventory[index] = (name, new_quantity)
            save_inventory()

            print("Quantity updated successfully.")
        else:
            print("Invalid number.")

    except ValueError:
        print("Please enter a valid number.")


# Delete item
def delete_item():
    view_inventory()

    if not inventory:
        return

    try:
        index = int(input("Enter item number to delete: ")) - 1

        if 0 <= index < len(inventory):
            removed = inventory.pop(index)
            save_inventory()

            print(f"Deleted: {removed[0]}")
        else:
            print("Invalid number.")

    except ValueError:
        print("Please enter a valid number.")


# Main program
def main():
    load_inventory()

    while True:
        show_menu()

        choice = input("Choose an option: ")

        if choice == "1":
            add_item()

        elif choice == "2":
            view_inventory()

        elif choice == "3":
            update_item()

        elif choice == "4":
            delete_item()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()