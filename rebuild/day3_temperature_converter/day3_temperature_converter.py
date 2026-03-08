#while loop
#if and elif
#input

while True:

    print("\n=== Temperature Converter ===")

    temperature = float(input("Enter temperature: "))
    unit = input("Convert from (C/F): ")

    if unit.upper() == "C":
        result = (temperature * 9/5) + 32
        print(f"{temperature}°C = {result}°F")

    elif unit.upper() == "F":
        result = (temperature - 32) * 5/9
        print(f"{temperature}°F = {result}°C")

    else:
        print("Invalid unit.")

    again = input("Convert again? (yes/no): ")

    if again.lower() != "yes":
        break

print("Converter closed.")