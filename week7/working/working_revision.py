import re
#                         |  OPTIONAL  |
#               Hours         Minutes     Period
#            (0-9|10-12)  :?  (00-59)?    (AM|PM)
PATTERN = r"([0-9]|1[0-2]):?([0-5][0-9])? (AM|PM)"
#    GROUPS:    1 & 4          2 & 5       3 & 6

def main():
    print(convert(input("Hours: ")))


def convert(s: str) -> str:
    """Convert a time range from 12-hour format to 24-hour format."""
    match = re.match(rf"^{PATTERN} to {PATTERN}$", s)
    if not match:
        raise ValueError
        
    start_time = convert_24h(
        int(match.group(1)),  # START HOUR
        int(match.group(2)) if match.group(2) else 0,  # START MINUTE, IF NONE SET TO 0
        match.group(3)  # START PERIOD, AM|PM
    )
    
    end_time = convert_24h(
        int(match.group(4)),  # END HOUR
        int(match.group(5)) if match.group(5) else 0,  # END MINUTE, IF NONE SET TO 0
        match.group(6)  # END PERIOD, AM|PM
    )
    
    return f"{start_time} to {end_time}"


def convert_24h(hour: int, minute: int, period: str) -> str:
    """Convert a single time from 12-hour format to 24-hour format."""
    if period == "AM" and hour == 12:  # 12AM SHOULD BE 0:00
        hour = 0
    elif period == "PM" and hour != 12:  # ADD 12 TO HOUR IF ITS 1PM-11PM
        hour += 12
    return f"{hour:02}:{minute:02}"  # RETURN IN 00:00 FORMAT


if __name__ == "__main__":
    main()
