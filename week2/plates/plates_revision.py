def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s: str) -> bool:
    return (2 <= len(s) <= 6
            and s[:2].isalpha()
            and s.isalnum()
            and (s.isalpha()
                 or number_check(s)))



def number_check(s: str) -> bool:
    for i, c in enumerate(s):
        if c.isdigit():
            return c != "0" and s[i:].isdigit()




main()


# Must start with 2+ LETTERS
# Char MIN = 2 | MAX = 6
# Numbers MUST come at the END, AAA222, X AAA22A
# First number used CANNOT be 0
# No punctuation/spaces
