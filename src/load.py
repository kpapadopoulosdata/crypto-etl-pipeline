import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "postgres"),
    "port": os.getenv("DB_PORT", "5432"),
    "dbname": os.getenv("POSTGRES_DB"),
    "user": os.getenv("POSTGRES_USER"),
    "password": os.getenv("POSTGRES_PASSWORD"),
}


def get_connection():
    return psycopg2.connect(**DB_CONFIG)


def load_records(records):
    conn = get_connection()
    cur = conn.cursor()

    insert_query = """
        INSERT INTO crypto_history
            (name, symbol, price, volume_24h, percent_change_24h, market_cap, fetched_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    for r in records:
        cur.execute(insert_query, (
            r["name"],
            r["symbol"],
            r["price"],
            r["volume_24h"],
            r["percent_change_24h"],
            r["market_cap"],
            r["fetched_at"],
        ))

    conn.commit()
    cur.close()
    conn.close()

    print(f"Loaded {len(records)} records into crypto_history.")


if __name__ == "__main__":
    from extract import fetch_top_crypto, parse_crypto_data

    raw = fetch_top_crypto(limit=50)
    records = parse_crypto_data(raw)
    load_records(records)