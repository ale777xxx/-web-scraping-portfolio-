# Microsoft Teams Scraper (Selenium)

A resilient proof-of-concept using **Selenium** + **BeautifulSoup** + **Pandas** to extract message history from Microsoft Teams channels and export to Excel/CSV.

> ⚠️ For demonstration/educational purposes. Use with accounts and workspaces you are authorized to access.

## Features
- Headless Chromium via Selenium
- Login flow with explicit waits
- Optional proxy support (env var `HTTP_PROXY` / `HTTPS_PROXY`)
- Structured export: `output/messages.xlsx`
- Retries & backoff on transient failures

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python teams_scraper.py --workspace https://teams.microsoft.com --export-format xlsx
```

## Environment
- Set proxies as needed:
```bash
export HTTP_PROXY="http://user:pass@host:port"
export HTTPS_PROXY="http://user:pass@host:port"
```
