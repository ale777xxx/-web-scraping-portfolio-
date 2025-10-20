# 🕷️ Web Scraping & Automation Portfolio

This repository showcases my hands-on expertise in **Python-based web scraping**, **browser automation**, and **proxy-network integration**.

I have **2+ years** of experience working with scraping tools and HTTP protocols, delivering reliable data pipelines, writing technical documentation, and supporting customers with clear, actionable communication.

## 🔭 What’s inside

- **Selenium automation**: Headless browsing, login flows, DOM parsing, structured exports, proxy support.
- **Scrapy crawlers**: Robust crawling (pagination, retries, throttling), pipelines, proxy & user-agent rotation.
- **Proxy rotation demos**: Residential/DC proxies, per-request rotation, session pinning, health checks.
- **Puppeteer (Node.js) demo**: Chromium control with proxy & stealth plugin.
- **Tests & fixtures**: Parsing helpers covered by pytest for correctness and maintainability.
- **Knowledge base**: Short articles with best practices and troubleshooting tips.
- **Docker**: Reproducible environment for Python projects.

> All projects are **educational** and demonstrate patterns I use in production with customer-grade quality.

---

## 📂 Projects

### 1) Selenium Teams Scraper
**Tech:** Python, Selenium, BeautifulSoup, Pandas, Tenacity  
Automates Microsoft Teams to extract messages (author, timestamp, text) into Excel/CSV. Includes login flow, explicit waits, proxy support, and resilient retry logic.

→ [Project Folder](./selenium_teams_scraper)

### 2) Scrapy E‑Commerce Crawler
**Tech:** Python, Scrapy, Pipelines, Middlewares  
Collects product data (name/price/rating) with UA + Proxy rotation, AutoThrottle, and clean CSV/JSONL exports.

→ [Project Folder](./scrapy_ecommerce)

### 3) Proxy Rotation Demo (Python)
**Tech:** Python, Requests, Selenium  
Demonstrates rotating proxies with health checks, backoff, and per-request identity verification.

→ [Project Folder](./proxy_rotation_demo)

### 4) Puppeteer Demo (Node.js)
**Tech:** Node.js, Puppeteer, Stealth Plugin  
Headless Chromium scraping with proxy and stealth evasion.

→ [Project Folder](./puppeteer_demo)

---

## 🧩 Skills demonstrated

- **Python 3.11+**, **Selenium WebDriver**, **Scrapy**, **BeautifulSoup4**
- **HTTP**: headers, cookies, sessions, rate limits, retries, backoff
- **Proxies**: residential/DC, rotation, session affinity, sticky IPs
- **Data shaping**: CSV / Excel exports with `pandas`
- **Testing**: `pytest` for parsing helpers and HTML fixtures
- **Docs**: Knowledge base articles (English, concise, practical)

---

## 🐳 Docker (optional)

Build a reproducible Python environment with dependencies for Selenium/Scrapy:

```bash
docker build -t scraping-portfolio .
docker run --rm -it -v $PWD:/app scraping-portfolio bash
```

---

## 🤝 Contact

- **GitHub:** https://github.com/ale777xxx
- **Email:** your.email@example.com

---

## 🪪 License

This project is released under the **MIT License**.
