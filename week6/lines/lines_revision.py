from sys import argv, exit


def main():
    if check_for_file():
        print(lines_of_code())


def check_for_file() -> bool:
    """
    Checks for valid command-line argument
        # Index must be 1
        # argument must be a python file
    """
    if len(argv) < 2:
        exit("Too few command-line arguments")

    elif len(argv) > 2:
        exit("Too many command-line arguments")

    if not argv[1].endswith(".py"):
        exit("Not a Python File")

    return True


def lines_of_code() -> int:
    """
    Opens existing file, reads line by line and only counts valid lines of code
    """
    try:
        file = open(argv[1]).read().splitlines()
        lines = 0

        for row in file:

            row = row.strip()

            # EMPTY STRINGS/LISTS AND COMMENTS RETURN FALSE
            if row and not row.startswith("#"):
                lines += 1

        return lines

    except FileNotFoundError:
        exit("File does not exist")


if __name__ == "__main__":
    main()
