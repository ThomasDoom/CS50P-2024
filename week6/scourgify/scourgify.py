from sys import argv, exit
import csv


fieldnames = ["first", "last", "house"]


def main():
    if check_for_files():
        new_data = open_file()
        write_file(new_data)


def check_for_files() -> bool:
    if len(argv) < 3:
        exit("Too few command-line arguments")

    elif len(argv) > 3:
        exit("Too many command-line arguments")

    if not (argv[1].endswith(".csv") or argv[2].endswith(".csv")):
        exit("Not a CSV File")

    return True


def open_file() -> list:
    #  CHECK FOR VALID CSV
    try:
        file = open(argv[1])
    except FileNotFoundError:
        exit(f"Could not read {argv[1]}")

    #  CREATE A DICTREADER OBJECT
    reader = csv.DictReader(file)

    converted_dict = []

    #  CONVERT THE READER OBJECT TO A NEW LIST OF DICTIONARIES WITH FIRST, LAST, HOUSE KEYS
    for row in reader:
        last, first = map(str, row['name'].split(", "))

        row = {
            'first': first,
            'last': last,
            'house': row['house']
        }

        converted_dict.append(row)

    return converted_dict


def write_file(new_file: list):
    #  CHECK FOR VALID CSV
    try:
        with open(argv[2], mode='w') as file:
    except AttributeError:
        exit(f"Could not write {argv[2]}")

    #  CREATE A DICTWRITER OBJECT WITH NEW FIELDNAMES
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # WRITE HEADER AND APPEND NEW DATA
    writer.writeheader()
    writer.writerows(new_file)


if __name__ == "__main__":
    main()

