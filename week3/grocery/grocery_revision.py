list = []
item_count: dict[str, int] = {}
# THIS LOOKS SO MUCH EASIER T-T

def main():
    """
    Get input, count their occurrences, and print the counts alphabetically
    """
    try:
        while True:
            item = input().upper()
            list.append(item)
    except EOFError:
        frequency_count()
        print_sorted_items(item_count)


def frequency_count():
    """
    Count frequency of items in list
    """
    for i in list:
        if not i in item_count:
            item_count[i] = 1
        else:
            item_count[i] += 1


def print_sorted_items(counts: dict[str, int]):
    """
    Prints the item counts sorted alpha by item names
    """
    for key, value in sorted(item_count.items()):
        print(value, key)


if __name__ == "__main__":
    main()
