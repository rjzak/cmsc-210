import random
import string
from datetime import date, timedelta

import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError
from django.utils.text import slugify
from tqdm import tqdm

from catalog.models import Cheese


class Command(BaseCommand):

    help = 'Bootstrap our database with the web scraper we wrote in lecture 14.'

    @staticmethod
    def get_soup(url):
        """Retrieve the HTML from a URL and convert it to tag soup."""
        return BeautifulSoup(requests.get(url).text, "html.parser")

    def get_detail_urls(self, max=None):
        """Retrieve a list of detail page URLs for all cheeses on the site."""
        urls = []
        print("Getting cheese detail URLs...")
        for letter in string.ascii_lowercase:  # Loop through each letter of the alphabet.
            # Construct the URL for the page listing all cheeses by letter of the alphabet:
            alphabet_index_url = f"https://cheese.com/alphabetical/?i={letter}"
            soup = self.get_soup(alphabet_index_url)
            for tag in soup.select(".cheese-item"):
                link = tag.select("h3 a")[0]
                href = link.attrs["href"]
                urls.append(f"https://cheese.com{href}")
            if max and len(urls) >= max:
                break
        return urls

    def get_cheese_data(self, url):
        """Retrieve cheese data from a detail page URL."""
        soup = self.get_soup(url)
        div = soup.find(class_="unit")
        data = {"name": div.find("h1").text.strip()}
        for tag in soup.find(class_="summary-points").children:
            cheese_property = tag.text
            if ":" in cheese_property:
                key, value = cheese_property.split(":")
                data[key] = value.strip()
        paras = []
        for index, paragraph in enumerate(soup.find(class_="description").select("p")):
            if index > 4:
                break
            paras.append(paragraph.text)
        data["description"] = "\n".join(paras)
        return data

    @staticmethod
    def random_date():
        start_date = date(2020, 5, 1)
        max_days = (date.today() - date(2020, 5, 1)).days
        return start_date + timedelta(days=random.randint(0, max_days))

    def handle(self, *args, **options):
        Cheese.objects.all().delete()
        self.stdout.write("All existing cheese records deleted.")
        cheese_urls = self.get_detail_urls(max=200)
        for url in tqdm(cheese_urls):
            data = self.get_cheese_data(url)
            slug = slugify(data["name"])
            cheese = Cheese(
                slug=slug,
                name=data["name"],
                description=data["description"],
                country_of_origin=data.get("Country of origin", ""),
                type=data.get("Type", ""),
                fat_content=round(random.uniform(0.1, 0.95), 3)
            )
            cheese.save()
            Cheese.objects.filter(slug=slug).update(last_updated=self.random_date())
        self.stdout.write("Done.")
