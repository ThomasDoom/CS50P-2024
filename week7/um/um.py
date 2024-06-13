import re

PATTERN = r"(\bum\b)"

def main():
    print(count(input("Text: ")))


def count(s: str) -> int:
    if match := re.findall(PATTERN, s, re.IGNORECASE):
        return len(match)


if __name__ == "__main__":
    main()
