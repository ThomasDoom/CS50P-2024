from random import randint

# EASILY CONFIGURABLE
MIN_LEVEL = 1
MAX_LEVEL = 3
NUM_QUESTIONS = 10
CHANCES = 3
MULTIPLIERS = [0, 1, 10, 100]


def main():
    level = get_level()
    score = get_score(level)
    print("Score:", score)


def get_score(level):
    score = 0
    for _ in range(NUM_QUESTIONS):
        if get_answer(level):
            score += 1
    return score


def get_answer(level):
    x = generate_integer(level)
    y = generate_integer(level)

    for _ in range(CHANCES):
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == x + y:
                return True

        # INVALID INPUT
        except ValueError:
            pass

        print("EEE")

    print(f"{x} + {y} = {x + y}")
    return False


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if MIN_LEVEL <= level <= MAX_LEVEL:
                return level

        # INVALID INPUT
        except ValueError:
            continue


def generate_integer(level: int) -> int:
    mn = 10 * MULTIPLIERS[level - 1]  # MIN RANGE 0, 10, 100
    mx = 10 * MULTIPLIERS[level]  # MAX RANGE 9, 99, 999
    return randint(mn, mx)


if __name__ == "__main__":
    main()
