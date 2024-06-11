import re

PATTERN = r'<iframe.*youtube\.com/embed/(\w+)'


def main():
    print(parse(input("HTML: ")))


def parse(s: str) -> str:
    if match := re.search(PATTERN, s):
        return f"https://youtu.be/{match.group(1)}"


if __name__ == "__main__":
    main()
