from random import randint

def main():
    while True:
        try:
            level = int(input("Level: "))
            answer = randint(1, level)
            guess_and_check(answer)
        except ValueError:
            pass


def guess_and_check(answer: int) -> str:
    while True:
        guess = int(input("Guess: "))
        if guess > answer:
            print("Too large!")
        elif guess < answer:
            print("Too small!")
        else:
            print("Just right!")
            quit()


if __name__ == "__main__":
    main()
