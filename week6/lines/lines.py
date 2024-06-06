import sys


def main():
    if check_for_file():
        print(lines_of_code())


def check_for_file() -> bool:
    """
    Checks for valid command-line argument
        # Index must be 1
        # argument must be a python file
    """
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python File")
    return True


def lines_of_code() -> int:
    """
    Opens existing file, reads line by line and only counts valid lines of code
    """
    try:
        with open(sys.argv[1]) as file:
            reader = file.readlines()

            line = 0

            for row in reader:
                row = row.replace('\n', '').strip()
                if row:
                    if "#" not in row[0]:
                        line += 1

            return line

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()

