while True:
    print("\n=== Simple Calculator ===")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")

    if operator == "+":git rm -r folder_name
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Cannot divide by zero"
    else:
        result = "Invalid operator"

    print(f"Result: {result}")

    again = input("Do you want to calculate again? (yes/no): ")
    if again.lower() != "yes":
        break

print("Calculator closed.")