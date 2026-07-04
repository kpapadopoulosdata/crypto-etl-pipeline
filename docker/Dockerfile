FROM python:3.12-slim

RUN apt-get update && apt-get install -y cron && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY docker/cron_job /app/cron_job

RUN crontab /app/cron_job

RUN mkdir -p /app/data/logs
RUN touch /app/data/logs/etl.log

CMD cron -f