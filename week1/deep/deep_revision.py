thought = input("What is the Answer to the Greatest Question of life, the Universe, and Everything? ").lower().strip()

if thought in ("42", "forty two", "forty-two"):
    print("Yes")
else:
    print("No")
