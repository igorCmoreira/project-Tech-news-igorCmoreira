import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
    selector = Selector(text=html_content)
    next_url = selector.css("a.next::attr(href)").get()
    if not next_url:
        return None
    return next_url


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    separator = ""
    return {
        "url": selector.css("link[rel='canonical']::attr(href)").get(),
        "title": (selector.css("h1.entry-title::text").get().strip()),
        "timestamp": selector.css("li.meta-date::text").get(),
        "writer": selector.css("li.meta-author span.author a::text").get(),
        "comments_count": len(selector.css("ol.comment-list").getall()),
        "summary": separator.join(
            selector.css(
                "div.entry-content > p:nth-of-type(1) *::text"
            ).getall()
        ).strip(),
        "tags": selector.css(".post-tags ul li a::text").getall(),
        "category": selector.css("a.category-style span.label::text").get()
    }


# Requisito 5
def get_tech_news(amount):
    link_news = []
    all_news = []
    current_page = "https://blog.betrybe.com"

    while len(link_news) < amount:
        content = fetch(current_page)
        urls = scrape_novidades(content)

        for url in urls:
            link_news.append(url)

        current_page = scrape_next_page_link(content)

    for news in link_news[:amount]:
        fetch_news = fetch(news)
        new_news = scrape_noticia(fetch_news)
        all_news.append(new_news)

    create_news(all_news)
    return all_news
