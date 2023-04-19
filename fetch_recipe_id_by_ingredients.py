import requests
import json
import pprint
from config import Spoon_API
from operator import itemgetter


APIKEY = Spoon_API
def load_data(ingredients, num_return):
    
    url=f"https://api.spoonacular.com/recipes/findByIngredients?apiKey={APIKEY}&ingredients={ingredients}&number={num_return}"
    f = requests.get(url)
    
    #converting bytes output into a list output
    response_bytes = f.content
    response_list= json.loads(response_bytes.decode('utf-8'))
    return response_list


def lookup_recipe_id(response_list):
#return lists of recipe_id, recipe_name, and used_incredients_count
    recipe_id = [i["id"] for i in response_list]
    # print(recipe_id)
    recipe_name =[i["title"] for i in response_list]
    # print(recipe_name)
    used_ingredients_count = [i["usedIngredientCount"] for i in response_list]
    # print(used_ingredients_count)

    #turning the information above to a dictionary under the recipe name key
    output_dict = {a:[b,c] for a,b,c in zip(recipe_name, recipe_id, used_ingredients_count)}
    return output_dict

def main():
    ingredients = "chicken, celery, apple"
    ingredients = ingredients.replace(', ', '%2C+')
    num_return = 5
    data = load_data(ingredients, num_return)
    recipe_info = lookup_recipe_id(data)
    return recipe_info

pprint.pprint(main())


