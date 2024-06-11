import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip: str) -> bool:
    """Initial check for [X.X.X.X] format, ONLY integers"""
    pattern = r"^\d+\.\d+\.\d+\.\d+$"

    return valid_bytes(ip) if re.match(pattern, ip) else False


def valid_bytes(ip: str) -> bool:
    """Final check for each number to be between 0-255"""
    bytes = ip.split(".")
    return all(0 <= int(byte) <= 255 for byte in bytes)


if __name__ == "__main__":
    main()
