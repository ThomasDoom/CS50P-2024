from sys import argv, exit


def main():
    if check_for_file():
        print(lines_of_code())


def check_for_file() -> bool:
    if len(argv) < 2:
        exit("Too few command-line arguments")
    elif len(argv) > 2:
        exit("Too many command-line arguments")

    if not argv[1].endswith(".py"):
        exit("Not a Python File")

    return True


def lines_of_code() -> int:
    """ Opens existing file, reads line by line and only counts valid lines of code """
    try:
        with open(sys.argv[1], 'r') as file:
            lines = (line.strip() for line in file)
            return sum(1 for line in lines if line and not line.startswith("#"))

    except FileNotFoundError:
        exit("File does not exist")


if __name__ == "__main__":
    main()
