#while loop
#if, elif, and else
#input
#break statement
#f strings
#continue

print("Simple Calculator")

while True:
    num1=float(input("Enter your first number: "))
    num2=float(input("Enter your second number: "))
    operator=input("Enter an operator (+, -, *, /): ")

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2 
        else:
            print("Cannot divide by zero")
            continue
    else:
        print("Invalid Operator")
        continue

    print(f"Result: {result}")
    
    again = input("Do you want to calculate again (y/n): ")
    if again.lower() != "y":
        break