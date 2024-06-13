import re
from sys import exit
#                      |  OPTIONAL  |                         |  OPTIONAL  |
#             (0-99)   (?: : (00-59))?   (AM|PM) to   (0-99)  (?: : (00-59))?   (AM|PM)
PATTERN = r"^(\d{1,2})(?::([0-5][0-9]))? (AM|PM) to (\d{1,2})(?::([0-5][0-9]))? (AM|PM)$"


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        exit(ValueError)

def convert(s: str):
    match = re.match(PATTERN, s)
    if not match:
        raise ValueError

    start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()

    start_hour = int(start_hour)
    start_minute = int(start_minute) if start_minute else 0
    end_hour = int(end_hour)
    end_minute = int(end_minute) if end_minute else 0

    if not (1 <= start_hour <= 12 or 0 <= end_hour <= 12):
        raise ValueError

    start_24 = convert_24h(start_hour, start_minute, start_period)
    end_24 = convert_24h(end_hour, end_minute, end_period)

    return f"{start_24} to {end_24}"


def convert_24h(hour: int, minute: int, period: str) -> str:
    if period == "AM" and hour == 12:
        hour = 0
    if period == "PM" and hour != 12:
        hour += 12
    return f"{hour:02}:{minute:02}"


if __name__ == "__main__":
    main()
