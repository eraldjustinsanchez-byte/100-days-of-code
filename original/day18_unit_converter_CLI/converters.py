# converters.py

from constants import LENGTH_UNITS, WEIGHT_UNITS, TIME_UNITS


def convert_linear(value, from_unit, to_unit, unit_map):
    if from_unit not in unit_map or to_unit not in unit_map:
        raise ValueError("Invalid unit")

    base_value = value * unit_map[from_unit]
    return base_value / unit_map[to_unit]


def convert_temperature(value, from_unit, to_unit):
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()

    if from_unit == "C":
        base = value
    elif from_unit == "F":
        base = (value - 32) * 5 / 9
    else:
        raise ValueError("Invalid temperature unit")

    if to_unit == "C":
        return base
    elif to_unit == "F":
        return base * 9 / 5 + 32
    else:
        raise ValueError("Invalid temperature unit")


def detect_category(from_unit, to_unit):
    if from_unit in LENGTH_UNITS and to_unit in LENGTH_UNITS:
        return "length"
    elif from_unit in WEIGHT_UNITS and to_unit in WEIGHT_UNITS:
        return "weight"
    elif from_unit in TIME_UNITS and to_unit in TIME_UNITS:
        return "time"
    elif from_unit.upper() in ["C", "F"] and to_unit.upper() in ["C", "F"]:
        return "temperature"
    else:
        return None


def convert(value, from_unit, to_unit):
    category = detect_category(from_unit, to_unit)

    if category == "length":
        return convert_linear(value, from_unit, to_unit, LENGTH_UNITS)
    elif category == "weight":
        return convert_linear(value, from_unit, to_unit, WEIGHT_UNITS)
    elif category == "time":
        return convert_linear(value, from_unit, to_unit, TIME_UNITS)
    elif category == "temperature":
        return convert_temperature(value, from_unit, to_unit)
    else:
        raise ValueError("Incompatible or unsupported units")