# apis.py

import requests
from config import NEWS_API_KEY

def fetch_news_from_api(query, api_key):
    """Obtiene noticias usando NewsAPI."""
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "language": "es",
        "sortBy": "publishedAt",
        "apiKey": NEWS_API_KEY,
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        noticias = response.json().get("articles", [])
        return [
            {"title": n["title"], "url": n["url"], "source": n["source"]["name"], "published_at": n["publishedAt"]}
            for n in noticias
        ]
    else:
        raise Exception(f"Error en NewsAPI: {response.status_code}, {response.text}")
