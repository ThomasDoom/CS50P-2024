def main():
    print(get_fuel("Fraction: "))


def get_fuel(prompt):
    while True:
        try:
            #  Gets input -> splits string into substrings and converts into integers
            num, den = map(int, input(prompt).split("/"))

            if num > den or den == 0:
                raise ValueError if num > den else ZeroDivisionError
            break
        except (ValueError, ZeroDivisionError):
            continue

    fuel_percentage = round(num / den * 100)
    if fuel_percentage <= 1:
        return "E"  # Empty
    elif fuel_percentage >= 99:
        return "F"  # Full
    return f"{fuel_percentage}%"  # Percentage


if __name__ == "__main__":
    main()


