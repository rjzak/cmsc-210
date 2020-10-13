from bs4 import BeautifulSoup
import requests


URL = "https://cheese.com/bleu-dauvergne/"


def get_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')


def cheese_properties(soup):
    attributes = {}
    for li in soup.select("ul.summary-points li p"):
        list_item = li.text
        if ":" in list_item:
            attribute, value = list_item.split(":")
            attributes[attribute.strip()] = value.strip()
    return attributes
