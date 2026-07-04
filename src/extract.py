import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timezone

load_dotenv()

API_KEY = os.getenv("COINMARKETCAP_API_KEY")
BASE_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"


def fetch_top_crypto(limit=50):
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": API_KEY,
    }
    params = {
        "start": "1",
        "limit": str(limit),
        "convert": "USD",
    }

    response = requests.get(BASE_URL, headers=headers, params=params)
    response.raise_for_status()
    return response.json()


def parse_crypto_data(raw_data):
    parsed = []
    fetch_time = datetime.now(timezone.utc)

    for coin in raw_data["data"]:
        quote = coin["quote"]["USD"]
        parsed.append({
            "name": coin["name"],
            "symbol": coin["symbol"],
            "price": quote["price"],
            "volume_24h": quote["volume_24h"],
            "percent_change_24h": quote["percent_change_24h"],
            "market_cap": quote["market_cap"],
            "fetched_at": fetch_time.isoformat(),
        })

    return parsed


if __name__ == "__main__":
    raw = fetch_top_crypto(limit=50)
    records = parse_crypto_data(raw)

    for r in records[:10]:
        print(f"{r['name']} ({r['symbol']}): ${r['price']:,.2f} | 24h change: {r['percent_change_24h']:+.2f}%")

    print(f"\nTotal records fetched: {len(records)}")