from random import randint

def main():
    # Loop till user wins
    while True:
        try:
            # Get level
            level = get_positive_integer("Level: ")

            # Generate random answer based on level
            answer = randint(1, level)

            # Start guessing game
            guess_and_check(answer)

        # Catch invalid inputs
        except (ValueError, Exception):
            pass


def get_positive_integer(prompt) -> int:
    level = int(input(prompt))

    if level > 0:
        return level

    # Non-positive integer
    raise Exception


def guess_and_check(answer: int) -> str:
    while True:
        guess = int(input("Guess: "))

        # Feedback for each guess to answer
        if guess > answer:
            print("Too large!")
        elif guess < answer:
            print("Too small!")
        else:
            print("Just right!")
            quit()


if __name__ == "__main__":
    main()
