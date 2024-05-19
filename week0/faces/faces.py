def main():
    string = input()
    print(convert(string))

def convert(txt):
    txt = txt.replace(":(", '🙁')
    txt = txt.replace(":)", '🙂')
    return txt

if __name__ == "__main__":
    main()
