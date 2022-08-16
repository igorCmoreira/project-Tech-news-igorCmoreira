from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    found = []
    for news in search_news({"title": {"$regex": title, "$options": "i"}}):
        found.append((news["title"], news["url"]))
    return found


# Requisito 7
def search_by_date(date):
    try:
        # date config
        dated = "%d/%m/%Y"
        datef = "%Y-%m-%d"
        # -----------------

        founded_news = []

        for news in search_news(
            {"timestamp": datetime.strptime(date, datef).strftime(dated)}
        ):
            founded_news.append((news["title"], news["url"]))

        return founded_news
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    news = search_news({"tags": {"$regex": tag, "$options": "-i"}})

    founded_news = []

    for n in news:
        founded_news.append((n["title"], n["url"]))
    return founded_news


# Requisito 9
def search_by_category(category):
    news = search_news({"category": {"$regex": category, "$options": "i"}})

    founded_news = []

    for n in news:
        founded_news.append((n["title"], n["url"]))

    return founded_news
