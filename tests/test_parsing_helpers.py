import re

def parse_price(text: str):
    # very basic price parser for demonstration
    m = re.search(r"(\d+[\.,]?\d*)", text or "")
    return float(m.group(1).replace(",", ".")) if m else None

def test_parse_price():
    assert parse_price("$12.99") == 12.99
    assert parse_price("EUR 1,234") == 1234.0
    assert parse_price("") is None
