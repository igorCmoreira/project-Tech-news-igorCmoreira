import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        if response.status_code != 200:
            time.sleep(1)
            return None
        response.headers["user-agent"] = "Fake user-agent"
        time.sleep(1)
        return response.text
    except requests.Timeout:
        time.sleep(1)
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    urls = []
    for url in selector.css("a.cs-overlay-link::attr(href)").getall():
        urls.append(url)
    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
