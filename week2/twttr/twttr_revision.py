word = input("Input: ")

output = ""

for c in word:
    if c not in 'AEIOUaeiou':
        output += c

print("Output:", output)
