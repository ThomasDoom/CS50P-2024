import re
#                         |  OPTIONAL  |
#               Hours         Minutes     Period
#            (0-9|10-12)  :?  (00-59)?    (AM|PM)
PATTERN = r"([1-9]|1[0-2]):?([0-5][0-9])? (AM|PM)"
#    GROUPS:    1 & 4          2 & 5       3 & 6

def main():
    print(convert(input("Hours: ")))


def convert(s: str):
    if match := re.match(r"^" + PATTERN + " to " + PATTERN + "$", s):
        start_time = convert_24h(int(match.group(1)),
                                 int(match.group(2)) if match.group(2) else 0,
                                 match.group(3)
                                 )
        end_time = convert_24h(int(match.group(4)),
                               int(match.group(5)) if match.group(5) else 0,
                               match.group(6)
                               )
        return f"{start_time} to {end_time}"
    else:
        raise ValueError


def convert_24h(hour: int, minute: int, period: str) -> str:
    if period == "AM" and hour == 12:
        hour = 0
    elif period == "PM" and hour != 12:
        hour += 12
    return f"{hour:02}:{minute:02}"


if __name__ == "__main__":
    main()
