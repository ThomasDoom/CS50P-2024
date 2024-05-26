from random import randrange


def main():
    level = get_game_level()

    # Level's answer
    answer = randrange(level + 1)

    # Loop until user wins
    while True:

        # Store users guess
        guess = get_user_guess()

        # Store and print result for each guess
        result = check_game(guess, answer)
        print(result)

        # End game if user wins
        if result != "Just right!":
            continue
        else:
            break


def get_game_level() -> int:

    # Loop until user inputs a positive integer
    while True:
        try:
            level = int(input("Level: "))

            # Check for positive integer
            if level > 0:
                return level

        # Retry loop if input is not an integer
        except ValueError:
            continue


def get_user_guess() -> int:

    # Loop until user inputs a positive integer
    while True:
        try:
            guess = int(input("Guess: "))

            # Check for positive integer
            if 0 < guess:
                return guess

        # Retry loop if input is not an integer
        except ValueError:
            pass


def check_game(guess: int, answer: int) -> str:

    # Check if guess is less, more, or equal to the answer
    if guess < answer:
        return "Too small!"
    elif guess > answer:
        return "Too large!"
    else:
        return "Just right!"


if __name__ == "__main__":
    main()

