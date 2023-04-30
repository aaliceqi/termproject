import requests
import json
import pprint
from config import Spoon_API

APIKEY = Spoon_API
def load_data(ingredients, num_return, ranking):
    
    url=f"https://api.spoonacular.com/recipes/findByIngredients?apiKey={APIKEY}&ingredients={ingredients}&number={num_return}&ranking={ranking}"
    return url
    
def read_data(url):
    """
    This function converts bytes from a url to a list
    """
    f = requests.get(url)
    response_bytes = f.content
    response_list= json.loads(response_bytes.decode('utf-8'))
    return response_list


def lookup_recipe_id(response_list):
    recipe_id_list = [] 
    for recipe in response_list:
        missed_ingredients = [ingredient["name"] for ingredient in recipe["missedIngredients"]]
        unused_ingredients = [ingredient["name"] for ingredient in recipe["unusedIngredients"]]
        recipe_id = {
            "id" : recipe["id"],
            "missing ingredients": missed_ingredients,
            "unused ingredients": unused_ingredients
        }
        recipe_id_list.append(recipe_id)
    return recipe_id_list


def main():
    ingredients = "chicken, celery, apple"
    ingredients = ingredients.replace(', ', '%2C+')
    num_return = 5
    ranking = 1 #1 for maximize used ingredient, 2 for minimize missing ingredients
    url = load_data(ingredients, num_return, ranking)
    data = read_data(url)
    recipe_info = lookup_recipe_id(data)
    return recipe_info
    # return data

# pprint.pprint(main())


