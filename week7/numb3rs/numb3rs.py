import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip: str) -> bool:
    """
    Initial check for [X.X.X.X] format, ONLY integers
    """
    return valid_integer(ip) if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip) else False


def valid_integer(ip: str) -> bool:
    """
    Final check for each number to be between 0-255
    """
    nums = tuple(map(int, ip.split(".")))
    return all(0 <= num <= 255 for num in nums)


if __name__ == "__main__":
    main()
