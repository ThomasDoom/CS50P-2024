months: list[str] = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def main():
    while True:
        date = input("Date: ")

        try:
            if "/" in date:
                # PARSE NUMERIC DATE IN [MM/DD/YYYY] FORMAT
                month, day , year = map(int, date.split("/"))

            else:
                # PARSE TEXTUAL DATE IN [Month Day, Year] FORMAT
                month, day, year = date.strip().title().split()
                day, year = int(day[:-1]), int(year)
                month = months.index(month) + 1

            # VALIDATE MONTH AND DAY RANGES
            if month <= 12 and day <= 31:
                break
              
        # INCORRECTLY FORMATTED DATE INPUT
        except (ValueError, KeyError):
            continue

    # PRINT DATE IN [YYYY-MM-DD] FORMAT
    print(f"{year:04}-{month:02}-{day:02}")

if __name__ == "__main__":
    main()
# i could rewrite this with helper functions inside of main() to make it nicer and more maintainable but this problem took all my patience and tears
# so we're copin with one big main function for now
