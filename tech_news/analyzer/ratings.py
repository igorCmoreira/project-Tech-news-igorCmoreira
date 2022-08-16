from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news = find_news()
    sort = sorted(news, key=lambda x: x["comments_count"], reverse=True)

    top_news = []

    for n in sort[:5]:
        top_news.append((n["title"], n["url"]))

    return top_news


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
