import re

PATTERN = r"(\bum\b)"

def main():
    print(count(input("Text: ")))


def count(s: str) -> int:
    return len(re.findall(PATTERN, s, re.IGNORECASE)):


if __name__ == "__main__":
    main()
