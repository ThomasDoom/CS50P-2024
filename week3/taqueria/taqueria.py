menu: dict[str, float]= {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    """
    User can order items off the menu.
    Each correctly inputted item is totaled to their 'bill'.
    [CTRL + D] {EOFError} to end their order.
    """
    bill = 0

    while True:
            try:
                user_order = input("Item: ").title() # Input formatted to match dict
                if user_order in menu:
                    bill += menu[user_order] # Add's int value to bill
                    print(f"Total: ${bill:.2f}") # Displays bill after proper input
            except EOFError:
                print() # New line for bash
                break
            except KeyError:
                pass


if __name__ == "__main__":
     main()
