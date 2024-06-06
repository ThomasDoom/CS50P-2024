import sys
from tabulate import tabulate
from csv import DictReader

def main():
    if check_for_file():
        get_menu()


def check_for_file() -> bool:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV File")

    return True


def get_menu() -> None:
    try:
        with open(sys.argv[1]) as menu:
          
            #  Shoulda looked more into the DictReader documentation oops
            print(tabulate(DictReader(menu), headers="keys", tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("CSV File not found")


if __name__ == "__main__":
    main()
