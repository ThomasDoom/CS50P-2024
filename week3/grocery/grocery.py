item_count: dict[str, int] = {}
# THIS TOOK FOREVER TO FIGURE OUTTTTTT

def main():
    """
    Get input, count their occurrences, and print the counts alphabetically
    """
    try:
        while True:
            item = input().upper()
            if item in item_count:
                item_count[item] += 1
            else:
                item_count[item] = 1
    except EOFError:
        print_sorted_items(item_count)



def print_sorted_items(counts: dict[str, int]):
    """
    Prints the item counts sorted alpha by item names
    """
    sorted_dict = {key: value for key, value in sorted(counts.items())} # I OVERCOMPLICATED THIS SO MUCH HAHAHHAA
    for key, value in sorted_dict.items():
        print(f'{value} {key}')


if __name__ == "__main__":
    main()
