CREATE TABLE IF NOT EXISTS crypto_history (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    symbol VARCHAR(20) NOT NULL,
    price NUMERIC(20, 8) NOT NULL,
    volume_24h NUMERIC(20, 2),
    percent_change_24h NUMERIC(10, 4),
    market_cap NUMERIC(25, 2),
    fetched_at TIMESTAMP NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_crypto_symbol ON crypto_history(symbol);
CREATE INDEX IF NOT EXISTS idx_crypto_fetched_at ON crypto_history(fetched_at);