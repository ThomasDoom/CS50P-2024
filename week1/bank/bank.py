# Gather input
greeting = input("Greeting: ").lower().strip()

what = "$100"
hey = "$20"
hello = "$0"

# Identify and sort input
if "hello" in greeting:
    print(hello)
elif greeting[0] == "h":
    print(hey)
else:
    print(what)
