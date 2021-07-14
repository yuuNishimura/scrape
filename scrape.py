
import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        articles = set()
        for tag in sp.find_all("a"):
            article = tag.get("href")
            if article is None:
                continue
            if "articles" in article:
                articles.add(article) if article not in articles else None

        urls = set()
        for i, article in enumerate(articles):

            r = urllib.request.urlopen(self.site + article[2:])
            html = r.read()
            parser = "html.parser"
            sp = BeautifulSoup(html, parser)
            title = sp.find('title').text.replace("Google News - ", "")

            if len(title) > 0:
                for tag in sp.find_all("a"):
                    url = tag.get("href")
                    if url is None:
                        continue
                    if "html" in url:
                        urls.add(url)

        with open(r"scrape.txt", "w", encoding="utf8") as f:
            for url in urls:
                f.write(f"{url}\n")


if __name__ == '__main__':
    news = "https://news.google.com/"
    Scraper(news).scrape()