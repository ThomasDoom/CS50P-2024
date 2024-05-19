def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    new_d = d.replace("$", "")
    return float(new_d)

def percent_to_float(p):
    new_p = p.replace("%", "")
    p_dec = float(new_p) / 100
    return p_dec

if __name__ == "__main__":
    main()
