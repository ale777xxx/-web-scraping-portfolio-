import os
import time
import random
import requests
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

PROXIES = [
    "http://user:pass@proxy1.example:8000",
    "http://user:pass@proxy2.example:8000",
    "http://user:pass@proxy3.example:8000",
]

def pick_proxy():
    return random.choice(PROXIES)

@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=1, max=10),
       retry=retry_if_exception_type((requests.RequestException,)))
def fetch_with_proxy(url: str) -> str:
    proxy = pick_proxy()
    proxies = {"http": proxy, "https": proxy}
    r = requests.get(url, proxies=proxies, timeout=15)
    r.raise_for_status()
    return r.text

if __name__ == "__main__":
    for i in range(3):
        html = fetch_with_proxy("https://httpbin.org/ip")
        print(html.strip())
        time.sleep(1)
