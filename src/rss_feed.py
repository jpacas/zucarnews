# rss_feed.py

import feedparser

def fetch_news_from_rss(feeds):
    """Extrae noticias desde múltiples feeds RSS."""
    noticias = []
    for feed_url in feeds:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            noticias.append({"title": entry.title, "url": entry.link, "source": feed.feed.title})
    return noticias
