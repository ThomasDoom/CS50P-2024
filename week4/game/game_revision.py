from random import randint

def main():
    # Loop till user wins
    while True:
        try:
            level = get_user_input()

            # Generate answer and start game
            answer = randint(1, level)
            guess_and_check(answer)

        # For non-integers
        except (ValueError, Exception):
            pass


def get_user_input() -> int:
    level = int(input("Level: "))

    # Check for positive integer
    if level > 0:
        return level

    # Fail case for negative integer and 0
    raise Exception


def guess_and_check(answer: int) -> str:
    while True:
        guess = int(input("Guess: "))

        # Determine loss or win (less, more, equal)
        if guess > answer:
            print("Too large!")
        elif guess < answer:
            print("Too small!")
        else:
            print("Just right!")
            quit()


if __name__ == "__main__":
    main()
