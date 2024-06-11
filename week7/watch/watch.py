import re


def main():
    print(parse(input("HTML: ")))


def parse(s: str) -> str:
    """Search through iframe to find youtube link, group and return the embed code with the shortened URL"""
    pattern = r'<iframe.*youtube\.com/embed/(\w+)'

    if match := re.search(pattern, s):
        url = match.group(1)
        return f"https://youtu.be/{url}"
    return None


if __name__ == "__main__":
    main()
