def main():
    print(get_fraction("Fraction: "))


def get_fraction(prompt):
    while True:
        try:
            frac = (input(prompt))
            x, y = frac.split("/")
            x, y = int(x), int(y)
            if x <= y:
                fuel = (int(x) / int(y)) * 100
                if 99 <= fuel <= 100:
                    return "F"
                elif 0 <= fuel <= 1:
                    return "E"
                elif 1 < fuel < 99:
                    return f"{round(fuel)}%"
                else:
                    pass
        except ValueError or ZeroDivisionError:
            pass


if __name__ == "__main__":
    main()

