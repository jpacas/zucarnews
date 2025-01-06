import requests
from bs4 import BeautifulSoup

def scrape_news(site_config):
    """Realiza scraping de un sitio."""
    try:
        response = requests.get(site_config["url"])
        print(f"Status Code para {site_config['url']}: {response.status_code}")
        if response.status_code != 200:
            raise Exception(f"Error al acceder al sitio: {site_config['url']}")

        soup = BeautifulSoup(response.content, "html.parser")
        articles = soup.find_all(site_config["article_tag"])

        noticias = []
        for article in articles:
            title = article.find(site_config["title_tag"]).text.strip()
            link = article.find(site_config["link_tag"])["href"]
            noticias.append({"title": title, "url": link, "source": site_config["name"]})

        return noticias

    except Exception as e:
        print(f"Error al procesar {site_config['url']}: {e}")
        return []
