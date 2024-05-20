def main():
    word = input("Input: ")
    output = ""

    for c in word:
        if is_not_vowel(c):
            output += c

    print("Output:", output)


def is_not_vowel(c):
    if c not in 'AEIOUaeiou':
        return True


if __name__ == "__main__":
    main()
