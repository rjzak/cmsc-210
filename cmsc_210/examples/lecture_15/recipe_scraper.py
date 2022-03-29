from bs4 import BeautifulSoup
from requests import get


def get_soup(url):
    """Retrieve the HTML from a URL and convert it to tag soup."""
    return BeautifulSoup(get(url).text, "html.parser")


if __name__ == "__main__":
    with open("test_recipe.html") as file:
        html = file.read()
