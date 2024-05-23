import emoji

def main():
    code_emoji = input("Input: ")
    print("Output:", emoji.emojize(code_emoji, language="alias"))

main()
