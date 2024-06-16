grocery_list: dict[str, int] = {}
# THIS LOOKS SO MUCH NICER T-T

def main():
    """
    Get input, count their occurrences, and print the counts alphabetically
    """
    frequency_count(grocery_list)
    print_sorted_items(grocery_list)


def frequency_count(list: dict[str, int]) -> None:
    """
    Count frequency of items in list
    """
    while True:
        try:
            item = input().upper()
        except EOFError:
            break
        else:
            try:
                list[item] += 1
            except KeyError:
                list[item] = 1


def print_sorted_items(list: dict[str, int]) -> str:
    """
    Prints the item counts sorted alpha by item names
    """
    for key, value in sorted(list.items()): # look how less complicated this is with a better result LOL
        print(value, key)


if __name__ == "__main__":
    main()
