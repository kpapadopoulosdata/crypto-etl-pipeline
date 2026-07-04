from extract import fetch_top_crypto, parse_crypto_data
from load import load_records


def run_pipeline():
    print("Starting ETL pipeline run.")

    raw = fetch_top_crypto(limit=50)
    records = parse_crypto_data(raw)
    load_records(records)

    print("ETL pipeline run complete.")


if __name__ == "__main__":
    run_pipeline()