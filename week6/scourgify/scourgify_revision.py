from sys import argv, exit
import csv


def main():
    #  GET VALID CSV FILES
    input_file, output_file = validate_arguments(argv)
    #  REFORMAT INPUT DATA
    new_data = read_input(input_file)
    #  WRITE REFORMATTED DATA TO OUTPUT
    write_output(output_file, new_data)


def validate_arguments(args) -> tuple:
    if len(args) != 3:
        sys.exit("Usage: python scourgify.py input.csv output.csv")

    if not (args[1].endswith(".csv") or args[2].endswith(".csv")):
        exit("Not a CSV File")

    return args[1], args[2]


def read_input(input_file) -> list:
    file = open_file(input_file, "r")
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
    file = open_file(output_file, "w")

    fieldnames = ["first", "last", "house"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(new_data)


def open_file(file, mode: str):
    try:
        return open(file, mode=mode)
    except FileNotFoundError:
        exit(f"Could not read {file}")


if __name__ == "__main__":
    main()
