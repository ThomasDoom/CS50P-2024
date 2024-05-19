def main():
    camel = input("camelCase: ")
    print("snake_case: " + snake_case(camel))

def snake_case(s):
    snake = []
    for c in s:
        if c.isupper():
            snake.append("_" + c)
        else:
            snake.append(c)
    return ''.join(snake).lower()


if __name__ == "__main__":
    main()

