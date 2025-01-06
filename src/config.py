# config.py

from dotenv import load_dotenv
import os


load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")


# URLs relevantes
RSS_FEEDS = [
    "https://www.sugarindustry.info/rss",
    "https://www.foodnavigator.com/rss"
]

SCRAPER_SITES = [
    {
        "name": "Sugar Industry News",
        "url": "https://www.sugarindustry.info/news",
        "article_tag": "article",
        "title_tag": "h2",
        "link_tag": "a"
    },
    {
        "name": "Food Navigator",
        "url": "https://www.foodnavigator.com/news",
        "article_tag": "div",
        "title_tag": "h3",
        "link_tag": "a"
    }
]

# Configuración de la base de datos
DATABASE_PATH = "data/noticias.db"
