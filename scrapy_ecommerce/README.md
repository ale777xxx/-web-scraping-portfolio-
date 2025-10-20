# Scrapy E‑Commerce Crawler

Demonstrates a robust Scrapy setup with **pagination**, **retries**, **proxy & user-agent rotation**, and clean exports.

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
scrapy crawl products -O outputs/products.csv
```

## Features
- Middleware: rotating User-Agent & optional proxy
- Settings: AutoThrottle, Retry, Download Delays
- Pipelines: item validation & normalization
