import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        
        # ვასუფთავებთ რობოტის მოწოდებულ მონაცემს მძიმეებისგან და ვაქცევთ სუფთა რიცხვად
        raw_price = str(data["bpi"]["USD"]["rate_float"]).replace(",", "")
        price = float(raw_price)
        
    except requests.RequestException:
        sys.exit()

    amount = bitcoins * price
    print(f"${amount:,.4f}")

if __name__ == "__main__":
    main()