import re
import time
from pathlib import Path
from urllib.parse import urljoin

import pandas as pd
import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.checkraka.com/motorcycle/'
OUTPUT = Path('.')
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/151.0.0.0 Safari/537.36',
    'Accept-Language': 'th-TH,th;q=0.9,en;q=0.8',
}
REQUEST_TIMEOUT = 20
REQUEST_DELAY = 1.0

session = requests.Session()
session.headers.update(HEADERS)


def fetch_page(url: str) -> str:
    response = session.get(url, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    return response.text


def normalize_link(href: str, base_url: str = BASE_URL) -> str:
    return urljoin(base_url, href.strip()) if href else ''


def text_of(node) -> str:
    return node.get_text(' ', strip=True) if node else ''


def extract_price_text(raw_text: str) -> str:
    # Require the unit to avoid confusing a model year with a price.
    match = re.search(r'[\d][\d,]*(?:\.\d+)?\s*(?:บาท|THB)', raw_text, re.I)
    return match.group(0).strip() if match else ''


def extract_motorcycle_rows(html: str, page_url: str):
    soup = BeautifulSoup(html, 'html.parser')
    rows = []
    detail_re = re.compile(r'^/motorcycle/[\w\-]+/[\w\-]+/\d+/?$')

    seen = set()
    for link in soup.find_all('a', href=True):
        href = link.get('href', '').strip()
        if not detail_re.match(href):
            continue
        detail_url = normalize_link(href, page_url)
        if detail_url in seen:
            continue
        seen.add(detail_url)
        card = link.parent
        raw = text_of(card)
        rows.append({
            'model_group': text_of(card),
            'variant': text_of(link),
            'price': extract_price_text(raw),
            'link': detail_url,
        })
    return rows


def scrape(url: str = BASE_URL):
    html = fetch_page(url)
    time.sleep(REQUEST_DELAY)
    return pd.DataFrame(extract_motorcycle_rows(html, url), columns=['model_group', 'variant', 'price', 'link'])


if __name__ == '__main__':
    df = scrape()
    df.to_csv(OUTPUT / 'raw_motorcycles.csv', index=False, encoding='utf-8-sig')
    print(f'Collected {len(df)} raw rows')
