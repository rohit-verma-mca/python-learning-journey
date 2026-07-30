def convert_temp(value, to_unit):
    if to_unit == "C":
        return (value - 32) * 5 / 9      # Fahrenheit -> Celsius
    elif to_unit == "F":
        return (value * 9 / 5) + 32      # Celsius -> Fahrenheit
    else:
        raise ValueError("to_unit must be 'C' or 'F'")


if __name__ == "__main__":
    print(convert_temp(98.6, "C"))   # Fahrenheit to Celsius -> 37.0
    print(convert_temp(37, "F"))     # Celsius to Fahrenheit -> 98.6
    print(convert_temp(0, "F"))      # Celsius to Fahrenheit -> 32.0