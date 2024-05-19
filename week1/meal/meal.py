def main():
    time = input("What time is it? ")
    c_time = convert(time)

    if 7 <= c_time <= 8:
        print("breakfast time")
    elif 12 <= c_time <= 13:
        print("lunch time")
    elif 18 <= c_time <= 19:
        print("dinner time")
    else:
        return


def convert(time):
    x, y = time.split(":")
    return float(x) + (float(y)/60)


if __name__ == "__main__":
    main()
