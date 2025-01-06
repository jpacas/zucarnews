# main.py

from config import NEWS_API_KEY, RSS_FEEDS, SCRAPER_SITES, DATABASE_PATH
from apis import fetch_news_from_api
from scraper import scrape_news
from rss_feed import fetch_news_from_rss
from db_manager import setup_database, save_news_to_db

def main():
    # Inicializar base de datos
    setup_database(DATABASE_PATH)

    # Recopilar noticias de NewsAPI
    print("Extrayendo noticias desde NewsAPI...")
    api_news = fetch_news_from_api("azúcar OR caña OR zafra", NEWS_API_KEY)

    # Recopilar noticias de scraping
    print("Realizando scraping...")
    scraped_news = []
    for site in SCRAPER_SITES:
        scraped_news.extend(scrape_news(site))

    # Recopilar noticias de RSS
    print("Extrayendo noticias desde RSS...")
    rss_news = fetch_news_from_rss(RSS_FEEDS)

    # Consolidar y guardar noticias
    all_news = api_news + scraped_news + rss_news
    save_news_to_db(DATABASE_PATH, all_news)

    print(f"¡Se han almacenado {len(all_news)} noticias nuevas!")

if __name__ == "__main__":
    main()
