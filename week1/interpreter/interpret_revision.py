def main():
    expr = input("Expression: ")
    print(convert(expr))

def convert(s):
    x, y, z = s.split(" ")
    x, z = float(x), float(z)

    match y:
        case "+":
            return(x + z)
        case "-":
            return(x - z)
        case "*":
            return(x * z)
        case "/":
            return(x / z)

if __name__ == "__main__":
    main()
