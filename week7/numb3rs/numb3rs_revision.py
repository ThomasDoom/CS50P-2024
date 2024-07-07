import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip: str) -> bool:
    """Find [X.X.X.X] match, ONLY integers"""
    pattern = r"^\d+\.\d+\.\d+\.\d+$"
    return valid_bytes(ip) if re.match(pattern, ip) else False


def valid_bytes(ip: str) -> bool:
    """Validate each number is 0-255"""
    return all(0 <= int(byte) <= 255 for byte in ip.split("."))


if __name__ == "__main__":
    main()
