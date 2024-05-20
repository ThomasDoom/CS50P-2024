def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s: str) -> bool:
    if 2 <= len(s) <= 6 and s[:2].isalpha() and s.isalnum():
        if s.isalpha():
            return True
        else:
            return number_check(s)


def number_check(s: str) -> bool:
    nums = []
    if s[-1].isdigit():
        for c in range(len(s)):
            if s[c].isdigit():
                if s[c:].isdigit():
                    nums.append(s[c])
                else:
                    return False
        if nums[0] != "0":
            return True

        return False



main()
