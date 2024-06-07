from sys import argv, exit
import csv


fieldnames = ["first", "last", "house"]


def main():
    input_file, output_file = validate_arguments(argv)
    new_data = read_input(input_file)
    write_output(output_file, new_data)


def validate_arguments(args) -> tuple:
    if len(args) != 3:
        sys.exit("Usage: python scourgify.py input.csv output.csv")

    if not (args[1].endswith(".csv") or args[2].endswith(".csv")):
        exit("Not a CSV File")

    return args[1], args[2]


def read_input(input_file) -> list:
    try:
        file = open(input_file)
    except FileNotFoundError:
        exit(f"Could not read {input_file}")

    reader = csv.DictReader(file)

    #  DEFINES NEW KEYS
    #  FOR EACH ROW IN THE INPUT, SPLIT INTO FIRST NAME, LAST NAME, HOUSE
    #  RETURNS RECONSTRUCTED LIST OF NEW DICTIONARIES
    return [
        {"first": first, "last": last, "house": row["house"]}
        for row in reader
        for last, first in [row["name"].split(", ")]
    ]


def write_output(output_file, new_data: list) -> None:
    try:
        file = open(output_file, mode='w')
    except Exception as e:
        exit(f"Could not write {output_file}: {e}")

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(new_data)


if __name__ == "__main__":
    main()
