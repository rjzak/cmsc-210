import requests
from bs4 import BeautifulSoup


class Recipe:
    def __init__(self, name, ingredients, steps):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps

    def __str__(self):
        lines = [self.name, "-" * 120, "Ingredients:"] + self.ingredients + ["-" * 120, "Steps:"] + self.steps
        return "\n".join(lines)


def clean_string(tag):
    string = tag.text.strip().replace("\n", "")
    new_string = ""
    last_char = ""
    for char in string:
        if char == " " and last_char == " ":
            pass
        else:
            new_string += char
        last_char = char
    return new_string


def scrape(
    html,
    name_selector='[itemprop="name"]',
    ingredient_selector='[itemprop="recipeIngredient"]',
    step_selector='[itemprop="step"]',
):
    soup = BeautifulSoup(html, "html.parser")
    name = clean_string(soup.select(name_selector)[0])
    ingredients = []
    for tag in soup.select(ingredient_selector):
        ingredients.append(clean_string(tag))
    steps = []
    for tag in soup.select(step_selector):
        steps.append(clean_string(tag))
    return Recipe(name, ingredients, steps)


def scrape_epicurious(html):
    return scrape(
        html,
        name_selector="h1",
        ingredient_selector='[itemprop="ingredients"]',
        step_selector=".preparation-step",
    )


def scrape_allrecipe(html):
    return scrape(
        html,
        name_selector="h1.headline",
        ingredient_selector=".ingredients-item-name",
        step_selector=".instructions-section-item",
    )


if __name__ == "__main__":
    html = requests.get("https://www.allrecipes.com/recipe/255588/chef-johns-chicken-a-la-king/").text
    recipe = scrape_allrecipe(html)
    print(recipe)
