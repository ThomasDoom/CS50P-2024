import sys
from pyfiglet import Figlet
from random import choice

f = Figlet()
fonts = f.getFonts()

try:
    if sys.argv[1] not in ('-f', '--font'):
        raise Exception
    f.setFont(font=sys.argv[2])

except IndexError:
    f.setFont(font=choice(fonts))

except (TypeError, Exception):
    sys.exit("Invalid Usage")


s = input("Input: ")

print("Output:\n", f.renderText(s))

