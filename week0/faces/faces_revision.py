def main():
    user_input = input()
    print(convert(user_input))

def convert(text):
    return text.replace(":(", '🙁').replace(":)", '🙂')

if __name__ == "__main__":
    main()
