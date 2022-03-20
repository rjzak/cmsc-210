"""
Go through all the cheeses listed on cheese.com and gather data about them.
"""
import string

import requests
from bs4 import BeautifulSoup


def get_soup(url):
    """Retrieve the HTML from a URL and convert it to tag soup."""
    return BeautifulSoup(requests.get(url).text, "html.parser")


def get_detail_urls():
    """Retrieve a list of detail page URLs for all cheeses on the site."""
    urls = []
    print("Getting cheese detail URLs...")
    for letter in string.ascii_lowercase:  # Loop through each letter of the alphabet.
        # Construct the URL for the page listing all cheeses by letter of the alphabet:
        alphabet_index_url = f"https://cheese.com/alphabetical/?i={letter}"
        soup = get_soup(alphabet_index_url)
        for tag in soup.select(".cheese-item"):
            link = tag.select("h3 a")[0]
            href = link.attrs["href"]
            urls.append(f"https://cheese.com{href}")
    return urls


def get_cheese_data(url):
    """Retrieve cheese data from a detail page URL."""
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


if __name__ == "__main__":
    main()
