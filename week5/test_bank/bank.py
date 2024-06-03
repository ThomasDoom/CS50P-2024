def main():
    greeting = input("Greeting: ")
    print(value(greeting))


def value(greeting: str):

    greeting = greeting.lower().strip()

    if "hello" in greeting:
        return 0
    if greeting.startswith('h'):
        return 20
    return 100

if __name__ == "__main__":
    main()
