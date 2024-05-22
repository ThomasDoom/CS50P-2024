months: list[str] = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    """
    Input date
    Check if it's arranged as "/" or ","
    Split elements from string into proper type variables
    Check valid dates
    Print in ISO 8601
    """
    while True:
        date = input("Date: ")

        if "/" in date:
            """
            If input date is formatted [XX/XX/XXXX]:
            Split date, convert each var into int
            Check if valid
            """
            try:
                month, day , year = [int(i) for i in date.split("/")]

            except KeyError:
                pass
            except ValueError:
                pass

            else:
                if month <= 12 and day <= 31:
                    break
                else:
                    pass

        elif "," in date:
            """
            If input date is formatted [Month X, XXXX]:
            Split date, check if day and year can be converted to int
            Remove comma
            Check if valid
            """
            try:
                month, day, year = date.strip().title().split(" ")
                day, year = int(day[:-1]), int(year)

            except KeyError:
                pass
            except ValueError:
                pass

            else:
                month = months.index(month) + 1
                if month <= 12 and day <= 31:
                    break
                else:
                    pass

        else:
            pass

    print(f"{year:04}-{month:02}-{day:02}")

if __name__ == "__main__":
    main()
