import requests
import time

def get_crypto_price(symbol):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    if symbol in data:
        return data[symbol]["usd"]
    else:
        return None

def track_crypto(symbol, interval=60):
    while True:
        price = get_crypto_price(symbol)
        if price is not None:
            print(f"{symbol.upper()} Price: ${price}")
        else:
            print(f"Failed to retrieve price data for {symbol.upper()}")
        time.sleep(interval)

if __name__ == "__main__":
    symbol = input("Enter the symbol of the cryptocurrency to track (e.g., bitcoin): ")
    track_crypto(symbol)
