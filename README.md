# Cryptocurrency Price Tracker 📈

This is a simple Python program that tracks the price of a cryptocurrency using the CoinGecko API.

## Requirements 🛠️

- Python 3.x
- requests library (`pip install requests`)

## Usage 🚀

1. Clone this repository:

```
git clone https://github.com/nikhiltamatta/cryptocurrency-price-tracker.git
```

2. Navigate to the project directory:

```
cd cryptocurrency-price-tracker
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Run the program:

```
python tracker.py
```

5. Enter the symbol of the cryptocurrency you want to track when prompted.

## Configuration ⚙️

You can change the default interval for fetching price data by editing the `interval` parameter in the `track_crypto` function in `tracker.py`.

## Example 💡

```
Enter the symbol of the cryptocurrency to track (e.g., bitcoin): bitcoin
BITCOIN Price: $37000
BITCOIN Price: $37050
BITCOIN Price: $37100
...
```

## Credits 🙏

- This program uses the CoinGecko API to fetch cryptocurrency price data.

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
