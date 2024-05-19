def main():
    camel = input("camelCase: ")
    print("snake_case:", convert_snake_case(camel))


def convert_snake_case(string):
    output = ""
    for c in string:
        if c.isupper():
            output += '_' + c.lower()
        else:
            output += c
    return output


if __name__ == "__main__":
    main()





# camel = input("camelCase: ")
# output = ""

# for c in camel:
#     if c.isupper():
#         output += '_' + c.lower()
#     else:
#         output += c

# print("snake_case:", output)
