def calculate_bmi(weight, height):
    return weight / (height ** 2)


while True:

    weight = float(input("\nEnter your weight (kg): "))
    height = float(input("Enter your height (m): "))

    bmi = calculate_bmi(weight, height)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    print(f"\nBMI: {round(bmi, 2)}")
    print("Category:", category)

    again = input("\nCalculate again? (yes/no): ").lower()

    if again != "yes":
        print("Goodbye!")
        break