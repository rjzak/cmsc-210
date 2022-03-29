from bs4 import BeautifulSoup
from requests import get


class Recipe:

    def __init__(self, name, ingredients, steps):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps

    def __str__(self):
        sep = "-" * 120
        lines = [self.name, sep] + self.ingredients + [sep] + self.steps
        return "\n".join(lines)


def get_soup(url):
    """Retrieve the HTML from a URL and convert it to tag soup."""
    return BeautifulSoup(get(url).text, "html.parser")


def clean_text(text):
    return text.strip()


def scrape(text, name_selector, ingredient_selector, step_selector):
    soup = BeautifulSoup(text, "html.parser")
    name = clean_text(soup.select(name_selector)[0].text)
    ingredients = []
    for tag in soup.select(ingredient_selector):
        ingredients.append(clean_text(tag.text))
    steps = []
    for tag in soup.select(step_selector):
        steps.append(clean_text(tag.text))
    return Recipe(name, ingredients, steps)


def scrape_schemaorg(text):
    return scrape(text,
                  name_selector='[itemprop="name"]',
                  ingredient_selector='[itemprop="recipeIngredient"]',
                  step_selector='[itemprop="recipeInstructions"] [itemprop="step"]'
                  )


def scrape_allrecipes(text):
    return scrape(text,
                  name_selector="h1.heading-content",
                  ingredient_selector="li.ingredients-item",
                  step_selector="li.instructions-section-item p"
                  )


def scrape_seriouseats(text):
    return scrape(text,
                  name_selector="h1.heading__title",
                  ingredient_selector="ul.ingredient-list li.ingredient",
                  step_selector="li.mntl-sc-block p.mntl-sc-block")


if __name__ == "__main__":
     # allrecipe = get("https://www.allrecipes.com/recipe/232552/caldereta-filipino-beef-and-chorizo-stew/").text
    # print(scrape_allrecipes(allrecipe))
    # with open("test_recipe.html") as file:
    #     html = file.read()
    #     recipe = scrape_schemaorg(html)
    #     print(recipe)
    se = get("https://www.seriouseats.com/pommes-dauphine-recipe-5217321").text
    print(scrape_seriouseats(se))
