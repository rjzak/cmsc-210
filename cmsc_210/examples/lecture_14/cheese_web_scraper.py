import string

import requests
from bs4 import BeautifulSoup

LISTING_URL = "https://cheese.com/alphabetical/?per_page=100"


def get_soup(url):
    return BeautifulSoup(requests.get(url).text, "html.parser")


def get_detail_urls():
    urls = []
    for letter in string.ascii_lowercase:
        alphabet_index_url = f"https://cheese.com/alphabetical/?i={letter}"
        soup = get_soup(alphabet_index_url)
        for tag in soup.select(".cheese-item"):
            link = tag.select("h3 a")[0]
            href = link.attrs["href"]
            urls.append(f"https://cheese.com{href}")
    return urls


def get_cheese_data(url):
    soup = get_soup(url)
    div = soup.find(class_="unit")
    data = {"name": div.find("h1").text.strip()}
    for tag in soup.find(class_="summary-points").children:
        cheese_property = tag.text
        if ":" in cheese_property:
            key, value = cheese_property.split(":")
            data[key] = value.strip()
    return data


def main():
    for url in get_detail_urls():
        data = get_cheese_data(url)
        print(data)
