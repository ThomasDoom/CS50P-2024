import re

PATTERN = r"^\d+\.\d+\.\d+\.\d+$"

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip: str) -> bool:
    """Find [X.X.X.X] match then return if each number is between 0-255"""
    if not re.match(PATTERN, ip):
        return False
    return all(0 <= int(byte) <= 255 for byte in ip.split("."))


if __name__ == "__main__":
    main()
