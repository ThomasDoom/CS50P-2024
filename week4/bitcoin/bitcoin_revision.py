import requests
import sys

try:
    rate = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()['bpi']['USD']['rate_float']
    amount = rate * float(sys.argv[1])
    print(f"${amount:,.4f}")
except (ValueError, IndexError):
    sys.exit("Invalid or missing command-line argument")
except requests.RequestException:
    sys.exit("Error fetching data from API")
