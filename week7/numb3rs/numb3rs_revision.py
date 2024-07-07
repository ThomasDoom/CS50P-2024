import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip: str) -> bool:
    """Find [X.X.X.X] match then return if each number is 0-255"""
    pattern = r"^\d+\.\d+\.\d+\.\d+$"
    if not re.match(pattern, ip):
        return False
    return all(0 <= int(byte) <= 255 for byte in ip.split("."))


if __name__ == "__main__":
    main()
