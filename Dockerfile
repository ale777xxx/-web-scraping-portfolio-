FROM python:3.11-slim

# System deps for Selenium/Chrome (headless) and Scrapy
RUN apt-get update && apt-get install -y     wget curl unzip gnupg build-essential chromium chromium-driver     && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install shared Python deps (optional)
COPY selenium_teams_scraper/requirements.txt /tmp/selenium-req.txt
COPY scrapy_ecommerce/requirements.txt /tmp/scrapy-req.txt
RUN pip install -U pip &&     pip install -r /tmp/selenium-req.txt &&     pip install -r /tmp/scrapy-req.txt

COPY . /app
CMD ["/bin/bash"]
