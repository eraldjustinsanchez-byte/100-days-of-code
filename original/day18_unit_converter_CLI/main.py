# main.py

from converters import convert
from utils import parse_input


def main():
    print("=== Unit Converter CLI ===")
    print("Format: <value> <from_unit> <to_unit>")
    print("Example: 100 cm m")
    print("Type 'exit' to quit")

    history = []

    while True:
        user_input = input("\n> ")

        if user_input.lower() == "exit":
            print("Good execution. Next.")
            break

        try:
            value, from_unit, to_unit = parse_input(user_input)
            result = convert(value, from_unit, to_unit)

            output = f"{value} {from_unit} = {result:.4f} {to_unit}"
            print(output)

            history.append(output)
            if len(history) > 10:
                history.pop(0)

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()