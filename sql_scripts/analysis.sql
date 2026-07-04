SELECT COUNT(*) AS total_records
FROM crypto_history;


SELECT symbol, COUNT(*) AS num_entries
FROM crypto_history
GROUP BY symbol
ORDER BY num_entries DESC;


SELECT MIN(fetched_at) AS earliest_fetch, MAX(fetched_at) AS latest_fetch
FROM crypto_history;


SELECT DISTINCT fetched_at
FROM crypto_history
ORDER BY fetched_at DESC
LIMIT 10;


SELECT name, symbol, price, fetched_at
FROM crypto_history
WHERE symbol = 'BTC'
ORDER BY fetched_at DESC
LIMIT 10;


SELECT symbol,
       MIN(price) AS min_price,
       MAX(price) AS max_price,
       AVG(price) AS avg_price
FROM crypto_history
WHERE symbol = 'BTC'
GROUP BY symbol;


SELECT name, symbol, price, percent_change_24h, fetched_at
FROM crypto_history
WHERE fetched_at = (SELECT MAX(fetched_at) FROM crypto_history)
ORDER BY percent_change_24h DESC
LIMIT 5;


SELECT name, symbol, price, percent_change_24h, fetched_at
FROM crypto_history
WHERE fetched_at = (SELECT MAX(fetched_at) FROM crypto_history)
ORDER BY percent_change_24h ASC
LIMIT 5;