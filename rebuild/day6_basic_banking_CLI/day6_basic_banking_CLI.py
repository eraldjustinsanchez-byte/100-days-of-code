#functions
#While loop
#if else and elif statements
#input

balance = 1000
running = True

def show_menu():
    print("\n===== BANK MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

def check_balance():
    print(f"Your balance is: ${balance}")

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))

    if amount > 0:
        balance += amount
        print(f"Deposited: ${amount}")
    else:
        print("Invalid amount.")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))

    if amount > balance:
        print("Insufficient balance.")
    elif amount > 0:
        balance -= amount
        print(f"Withdrawn: ${amount}")
    else:
        print("Invalid amount.")

while running:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        check_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        print("Goodbye!")
        running = False
    else:
        print("Invalid option.")