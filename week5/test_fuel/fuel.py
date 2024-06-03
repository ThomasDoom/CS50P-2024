def main():
    print(gauge(convert(input("Fraction: "))))

def convert(fraction: str) -> int:

    num, den = map(int, fraction.split("/"))

    if den == 0:
        raise ZeroDivisionError
    elif num > den:
        raise ValueError
    else:
        return round((num / den) * 100)


def gauge(percentage: int) -> str:
    if percentage <= 1:
        return "E"  # Empty
    elif percentage >= 99:
        return "F"  # Full
    else:
        return f"{percentage}%"  # Percentage


if __name__ == "__main__":
    main()
