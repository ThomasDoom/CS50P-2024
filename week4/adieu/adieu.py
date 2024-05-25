# ...... i didnt open the hint LOL

names = []
while True:
    try:
        name = input("Name: ")
        names.append(name)

    except EOFError:
        break

print("\nAdieu, adieu, to", end=' ')
if len(names) > 2:
    for n in names[:-1]:
        print(n, end=', ')
    print("and", names[-1])
elif len(names) == 2:
        print(names[0], "and", names[1])
else:
     print(names[0])
