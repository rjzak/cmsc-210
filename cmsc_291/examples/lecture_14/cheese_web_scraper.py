from bs4 import BeautifulSoup
import requests

URL = "https://cheese.com/bleu-dauvergne/"


def get_html(url):
    """Retrieve a URL and return the HTML content."""
    reponse = requests.get(url)
    return reponse.text


def get_info(html):
    """Fetch the summary points of information from an individual cheese page as a Python dictionary."""
    properties = {}
    soup = BeautifulSoup(html, 'html.parser')
    for li in soup.select(".summary-points li"):
        text = li.text
        if ":" in text:
            key, value = text.split(":")
            key = key.strip()
            value = value.strip()
            properties[key] = value
    return properties


def get_links():
    """Individual cheese detail page links from the listing of all cheeses."""
    links = []
    url = "https://cheese.com/alphabetical/?per_page=100&i=&page=1#top"
    soup = BeautifulSoup(get_html(url), "html.parser")
    for div in soup.select(".cheese-item"):
        link = div.find("a")
        if "href" in link.attrs:
            links.append("https://cheese.com{href}".format(href=link.attrs["href"]))
    return links


if __name__ == "__main__":
    for link in get_links():
        html = get_html(link)
        props = get_info(html)
        print(props)
