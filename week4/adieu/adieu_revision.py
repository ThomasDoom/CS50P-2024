# ....... i didnt open the hint LOL
import inflect

p = inflect.engine()
names = []

while True:
    try:
        names.append(input("Name: ").strip())
    except EOFError:
        print("\nAdieu, adieu, to", p.join(names))
        break
