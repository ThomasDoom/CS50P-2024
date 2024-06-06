from sys import argv, exit
from tabulate import tabulate
from csv import DictReader

def main():
    if check_for_file():
        get_menu()


def check_for_file() -> bool:
    if len(argv) < 2:
        exit("Too few command-line arguments")

    elif len(argv) > 2:
        exit("Too many command-line arguments")

    if not argv[1].endswith(".csv"):
        exit("Not a CSV File")

    return True


def get_menu() -> None:
    try:
        with open(argv[1]) as menu:

            #  Shoulda looked more into the DictReader documentation oops
            print(tabulate(DictReader(menu), headers="keys", tablefmt="grid"))

    except FileNotFoundError:
        exit("CSV File not found")


if __name__ == "__main__":
    main()
