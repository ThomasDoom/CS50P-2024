# Get intput
expr = input("Expression: ")

# Split string
x, y, z = expr.split(" ")
x, z = int(x), int(z)

# Filter y
# Print
match y:
    case "+":
        print(float(x + z))
    case "-":
        print(float(x - z))
    case "*":
        print(float(x * z))
    case "/":
        print(float(x / z))
