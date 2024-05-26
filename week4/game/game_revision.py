from random import randint


def main():
    level = get_game_level()
    answer = randint(1, level)
    while True:
        guess = get_user_guess()
        result = check_game(guess, answer)
        print(result)
        if result != "Just right!":
            continue
        else:
            break


def get_game_level() -> int:
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except ValueError:
            continue


def get_user_guess() -> int:
    while True:
        try:
            guess = int(input("Guess: "))
            if 0 < guess:
                return guess
        except ValueError:
            pass


def check_game(guess: int, answer: int) -> str:
    if guess < answer:
        return "Too small!"
    elif guess > answer:
        return "Too large!"
    else:
        return "Just right!"


if __name__ == "__main__":
    main()
