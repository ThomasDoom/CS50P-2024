def main():
    print(calculate_fuel_status("Fraction: "))


def calculate_fuel_status(prompt):
    """
    Calculate the fuel status based on the provided fuel fraction.
    Returns:
        - "F" for full,
        - "E" for empty,
        - Percentage for other cases.
    """
    while True:
        try:
            # Gets input -> splits string into substrings and converts into integers
            num, den = map(int, input(prompt).split("/"))

            # Checks for valid fraction and non-zero denominator
            if num <= den and den != 0:
                fuel_perc = round((num / den) * 100) # Decimal to percent value
                if fuel_perc <= 1:
                    return "E"  # Empty
                elif fuel_perc >= 99:
                    return "F"  # Full
                else:
                    return f"{fuel_per}%"  # Percentage

        except (ValueError, ZeroDivisionError):
            pass


if __name__ == "__main__":
    main()
