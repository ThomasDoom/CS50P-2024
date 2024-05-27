#  USER SPECIFIES A NUMBER AMOUNT OF BITCOIN [n] IN COMMAND LINE
#  IF AMOUNT ISN'T FLOAT -> EXIT PROGRAM VIA sys.exit WITH AN ERROR MSG
#  USE API TO GET AND PARSE JSON OBJECT FROM https://api.coindesk.com/v1/bpi/currentprice.json TO GET CURRENT PRICE OF BITCOIN
#  BE SURE TO CATCH AN EXCEPTIONS
#  OUTPUT CURRENT COST OF n BITCOIN TO 4 DECIMAL PLACES USING [,] AS A THOUSANDS SEPARATOR
import json
import requests
import sys

try:
    query = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    rate = query.json()['bpi']['USD']['rate_float']
    amount = rate * float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
except IndexError:
    sys.exit("Missing command-line argument")
else:
    print(f"Your amount of {sys.argv[1]} BTC is ${amount:,.4f}")

