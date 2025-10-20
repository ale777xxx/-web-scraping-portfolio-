import os
import time
import argparse
import pandas as pd
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

def build_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Proxy from env
    http_proxy = os.getenv("HTTP_PROXY") or os.getenv("HTTPS_PROXY")
    if http_proxy:
        options.add_argument(f"--proxy-server={http_proxy}")

    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(60)
    driver.implicitly_wait(5)
    return driver

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=10),
    retry=retry_if_exception_type(Exception),
    reraise=True,
)
def login_and_grab_html(driver, workspace_url: str) -> str:
    driver.get(workspace_url)
    # Example: wait for login field or app root
    WebDriverWait(driver, 30).until(
        EC.any_of(
            EC.presence_of_element_located((By.ID, "app")),  # app root
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
    )
    time.sleep(3)  # allow dynamic content to hydrate
    return driver.page_source

def parse_messages(html: str):
    soup = BeautifulSoup(html, "html.parser")
    # Fallback selectors for demo purposes
    candidates = soup.select("[data-tid='messageBody'], .message-body, .ts-message")
    rows = []
    for el in candidates:
        text = el.get_text(strip=True)
        if not text:
            continue
        # Fake/placeholder fields for PoC
        rows.append({
            "timestamp": "",
            "author": "",
            "message": text
        })
    return rows

def export_rows(rows, fmt="xlsx", outdir="output"):
    os.makedirs(outdir, exist_ok=True)
    if fmt == "xlsx":
        pd.DataFrame(rows).to_excel(os.path.join(outdir, "messages.xlsx"), index=False)
    else:
        pd.DataFrame(rows).to_csv(os.path.join(outdir, "messages.csv"), index=False)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workspace", default="https://teams.microsoft.com", help="Teams workspace URL")
    ap.add_argument("--export-format", choices=["xlsx", "csv"], default="xlsx")
    args = ap.parse_args()

    driver = build_driver()
    try:
        html = login_and_grab_html(driver, args.workspace)
        rows = parse_messages(html)
        export_rows(rows, args.export_format)
        print(f"Exported {len(rows)} messages.")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
