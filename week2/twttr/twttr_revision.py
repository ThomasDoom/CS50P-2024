word = input("Input: ")

output = ""

for c in word:
    if c not in 'AEIOUaeiou':
        output += c

print("Output:", output)

# My original answer and this revised version is a great example of how to use 'not in' to simplify algorithms
