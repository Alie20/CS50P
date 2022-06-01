import sys , requests

if  (len(sys.argv) != 2):
    sys.exit("Missing command-line argument")
else:
    try:
        money = float(sys.argv[1])
        try:
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            o = response.json()
            rate = (o["bpi"]["USD"]["rate"]).replace(",","")
            total = (float(rate)* money)
            print(f"${total:,.4f}")
        except requests.RequestException:
            pass
    except ValueError:
        sys.exit("Bitcoin is not a number")
