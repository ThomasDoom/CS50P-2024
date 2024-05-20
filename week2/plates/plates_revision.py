def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s: str) -> bool:
    return (2 <= len(s) <= 6 # Check length
            and s[:2].isalpha() # Check first 2 char are letters
            and s.isalnum() # Check for punctuation/spaces
            and (s.isalpha()
                 or number_check(s))) # If there are numbers go through function


def number_check(s: str) -> bool:
    for i, c in enumerate(s): # Enumerate = [(2, 'C'), (3, 'S'), (4, '5'), (5, '0')]
        if c.isdigit():
            return c != "0" and s[i:].isdigit() # Once first digit is found, check if 0 and check if remainder isdigit


main()


# Must start with 2+ LETTERS
# Char MIN = 2 | MAX = 6
# Numbers MUST come at the END, AAA222, X AAA22A
# First number used CANNOT be 0
# No punctuation/spaces
