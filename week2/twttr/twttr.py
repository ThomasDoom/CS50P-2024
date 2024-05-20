def main():
    word = input("Input: ")
    print("Output:", remove_vowels(word))


def remove_vowels(s) -> str:
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    result = ""

    # Check each char in s
    for c in s:

        # Ignore vowels
        if c in vowels:
            continue

        # Add else to 'result' string
        else:
            result += c

    return result


if __name__ == "__main__":
    main()
