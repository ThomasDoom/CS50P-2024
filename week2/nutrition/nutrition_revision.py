fruits: dict[str, int]= {
    "apple":           130,
    "banana":          110,
    "pear":            100,
    "sweet cherries":  100,
    "grapes":           90,
    "kiwifruit":        90,
    "orange":           80,
    "watermelon":       80,
    "plums":            70,
    "grapefruit":       60,
    "nectarine":        60,
    "peach":            60,
    "avocado":          50,
    "cantaloupe":       50,
    "honeydew melon":   50,
    "pineapple":        50,
    "strawberries":     50,
    "tangerine":        50,
    "lime":             20,
    "lemon":            15,
}

fruit = input("Item: ").lower()
if fruit in fruits:
    print("Calories:", fruits[fruit])

# // LOL nothing to really fix just thought I'd make it look nicer for fun
