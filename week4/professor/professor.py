from random import randint


def main():

    level = get_level()

    # INIT
    question = 0
    correct = 0

    while question < 10:
        # COUNT ERRORS
        eee = 0

        # GENERATE X AND Y
        x = generate_integer(level)
        y = generate_integer(level)

        while True:
            try:
                # USER INPUT TO X + Y
                answer = int(input(f"{x} + {y} = "))

                # CHECK IF INPUT INCORRECT
                if answer != x + y:
                    print("EEE")
                    eee += 1

                    # 3 STRIKES REVEAL ANSWER AND MOVE TO NEXT
                    if eee == 3:
                        print(f"{x} + {y} = {x+y}")
                        question += 1
                        break
                else:
                    question += 1
                    correct += 1
                    break
                
            # INVALID INPUT IS INCORRECT ANSWER
            except ValueError:
                print("EEE")
                eee += 1
                if eee == 3:
                    print(f"{x} + {y} = {x+y}")
                    question += 1
                    break

    print("Score:", correct)


def get_level():
    # INIT VALID LEVELS
    levels = [1, 2, 3]

    while True:
        try:
            level = int(input("Level: "))
            if level in levels:
                return level

        # CATCH INVALID INPUT
        except ValueError:
            continue


def generate_integer(level: int) -> int:
    # RANGE MULTI PER LEVEL
    multi = [0, 1, 10, 100]

    # MIN RANGE 0, 10, 100
    mn = 10 * multi[level - 1]

    # MAX RANGE 9, 99, 999
    mx = 10 * multi[level]

    return randint(mn, mx)


if __name__ == "__main__":
    main()
