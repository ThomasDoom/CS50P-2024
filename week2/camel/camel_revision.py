def main():
    camel = input("camelCase: ")
    print("snake_case:", snake_case(camel))


def snake_case(string):
    output = ""
    for c in string:
        if c.isupper():
            output += '_' + c.lower()
        else:
            output += c
    return output


if __name__ == "__main__":
    main()



# ALT WITHOUT FUNCTIONS

# camel = input("camelCase: ")
# output = ""

# for c in camel:
#     if c.isupper():
#         output += '_' + c.lower()
#     else:
#         output += c

# print("snake_case:", output)
