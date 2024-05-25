def main():
    names = []
    while True:
        try:
            # read and append names from user input until [CTRL + D]
            names.append(input("Name: ").strip())

        except EOFError:
            break

    # Format farewell using the collected names and print
    farewell = format_farewell(names)
    print(f"\nAdieu, adieu, to {farewell}")


def format_farewell(names):
    # If there is only 1 name, return it directly
    if len(names) == 1:
        return names[0]

    # If there are 2 names, join them with 'and
    elif len(names) == 2:
        return f"{names[0]} and {names[1]}"

    #If there are 3+ names, use commas and 'and' appropriately
    else:
        return f"{', '.join(names[:-1])}, and {names[-1]}"


if __name__ == "__main__":
    main()
