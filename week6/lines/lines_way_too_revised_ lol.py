import sys; sys.exit("Invalid argument") if len(sys.argv) != 2 or not sys.argv[1].endswith(".py") else None
try:
    print(sum(1 for line in open(sys.argv[1]) if line.strip() and not line.lstrip().startswith("#")))
except FileNotFoundError:
    sys.exit("File does not exist")

# HAHAHA the magic you can do with comprehensions (This is very bad code just to be clear i just wanted to see how crazy it can get ^_^)


# but this isnt even the best we can do
# you can go even further if u want
# behold...

import sys; sys.exit("Invalid argument") if len(sys.argv) != 2 or not sys.argv[1].endswith(".py") else print(sum(1 for line in open(sys.argv[1]) if line.strip() and not line.lstrip().startswith("#"))) if open(sys.argv[1]) else sys.exit("File does not exist")

# least confusing code right there. horrifying. it passes the check50 tho so its clearly optimal /s
# referenced @csfive's solution for this
