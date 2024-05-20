def main():
    print(get_fraction("Fraction: "))


def get_fraction(prompt):
    while True:
        try:
            frac = (input(prompt))

            # Turns both split substrings into integers
            x, y = map(int, frac.split("/"))

            # Checks for valid fraction
            if x <= y and y != 0:

                # Converting from decimal to percent value
                fuel: int = int(round((x / y) * 100))
                if fuel <= 1:
                    return "E"
                if fuel >= 99:
                    return "F"
                else:
                    return f"{fuel}%"
            else:
                pass
            
        except (ValueError, ZeroDivisionError):
            pass


if __name__ == "__main__":
    main()
