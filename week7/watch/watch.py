import re


def main():
    print(parse(input("HTML: ")))


def parse(s: str) -> str:
    """Search through iframe to find youtube link, group and return the embed code with the shortened URL"""
    try:
        match = re.search(r'<iframe?.*youtube\.com/embed+/(\w+)', s, re.IGNORECASE)
        embed = match.group(1)
        return f"https://youtu.be/{embed}"

    except Exception:
        return None


if __name__ == "__main__":
    main()
