import sys
from tabulate import tabulate

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


def get_menu():
    try:
        with open(sys.argv[1]) as menu:
            headers = []
            table = []
            for items in menu:
                row = []
                pizza, small, large = map(str, items.split(","))
                if not headers:
                    headers.append(pizza)
                    headers.append(small)
                    headers.append(large.strip())
                    continue

                row.append(pizza)
                row.append(small)
                row.append(large)

                table.append(row)
                
            print(tabulate(table, headers, tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("CSV File not found")


if __name__ == "__main__":
    main()

