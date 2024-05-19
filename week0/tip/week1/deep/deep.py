thought = input("What is the Answer to the Greatest Question of life, the Universe, and Everything? ").lower().strip()

if thought == "42":
    print("Yes")
elif thought == "forty two":
    print("Yes")
elif thought == "forty-two":
    print("Yes")
else:
    print("No")
