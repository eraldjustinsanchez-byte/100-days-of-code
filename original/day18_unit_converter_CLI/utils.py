# utils.py

def parse_input(user_input):
    parts = user_input.strip().split()

    if len(parts) != 3:
        raise ValueError("Format: <value> <from_unit> <to_unit>")

    value = float(parts[0])
    from_unit = parts[1].lower()
    to_unit = parts[2].lower()

    return value, from_unit, to_unit