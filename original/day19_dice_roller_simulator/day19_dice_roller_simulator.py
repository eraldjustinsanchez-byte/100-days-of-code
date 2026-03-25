import random
from collections import Counter

# ---------------------------
# INPUT HANDLING
# ---------------------------

def get_int_input(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"Enter a value between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Enter a number.")

# ---------------------------
# CORE LOGIC
# ---------------------------

def roll_dice(num_dice, sides):
    return [random.randint(1, sides) for _ in range(num_dice)]

# ---------------------------
# DISPLAY
# ---------------------------

def display_results(results):
    print("\n🎲 Rolling...")
    print(f"Results: {results}")
    print(f"Total: {sum(results)}")
    print("-" * 40)

def display_statistics(history):
    if not history:
        print("No rolls yet.")
        return

    flat_rolls = [num for roll in history for num in roll]

    print("\n📊 Statistics:")
    print(f"Total rolls: {len(history)}")
    print(f"All values: {flat_rolls}")
    print(f"Average roll: {sum(flat_rolls) / len(flat_rolls):.2f}")
    print(f"Highest roll: {max(flat_rolls)}")

    freq = Counter(flat_rolls)
    print("\nFrequency:")
    for value, count in sorted(freq.items()):
        print(f"{value}: {count}")

    print("-" * 40)

# ---------------------------
# MAIN APP
# ---------------------------

def play():
    history = []

    print("🎲 Advanced Dice Roller Simulator")

    while True:
        print("\nOptions:")
        print("1. Roll Dice")
        print("2. View Statistics")
        print("3. Exit")

        choice = input("Select option: ")

        if choice == '1':
            num_dice = get_int_input("Number of dice (1-10): ", 1, 10)
            sides = get_int_input("Number of sides (e.g. 6, 12, 20): ", 2, 100)

            results = roll_dice(num_dice, sides)
            history.append(results)

            display_results(results)

        elif choice == '2':
            display_statistics(history)

        elif choice == '3':
            print("Good execution. Next.")
            break

        else:
            print("Invalid option.")

# ---------------------------
# ENTRY POINT
# ---------------------------

if __name__ == "__main__":
    play()