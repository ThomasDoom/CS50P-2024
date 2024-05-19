due = 50

while True:
    print("Amount Due:", due)
    money = int(input("Insert Coin: "))
    if money == 5 or money == 10 or money == 25:
        if (money >= due):
            print("Change Owed:", money-due)
            break
        due -= money
    else:
        continue
