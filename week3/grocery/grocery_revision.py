grocery_list: dict[str, int] = {}
# THIS IS SO MUCH SIMPLER T-T

def main():
    """
    Get input, count their occurrences, and print the counts alphabetically
    """
    try:
        frequency_count(grocery_list)
    except EOFError:
        print_sorted_items(grocery_list)


def frequency_count(list: dict[str, int]) -> None:
    """
    Count frequency of items in list
    """
    while True:
        item = input().upper().strip()
        if not item in list:
            list[item] = 1
        else:
            list[item] += 1


def print_sorted_items(list: dict[str, int]) -> str:
    """
    Prints the item counts sorted alpha by item names
    """
    for key, value in sorted(list.items()):
        print(value, key)


if __name__ == "__main__":
    main()
