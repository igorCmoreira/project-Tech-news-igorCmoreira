from tech_news.database import find_news
from collections import Counter


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
    news = find_news()
    top_cate = []

    sort = Counter(sorted(n["category"] for n in news))
    categories = sort.most_common(5)

    for c in categories:
        top_cate.append(c[0])

    return top_cate
