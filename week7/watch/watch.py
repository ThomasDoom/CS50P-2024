import re

PATTERN = r'<iframe.*youtube\.com/embed/(\w+)'


def main():
    print(parse(input("HTML: ")))


def parse(s: str) -> str:
    """Search through iframe to find youtube link, group and return the embed code with the shortened URL"""
    if match := re.search(PATTERN, s):
        return f"https://youtu.be/{match.group(1)}"
    return None


if __name__ == "__main__":
    main()
