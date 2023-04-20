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
#return lists of recipe_id, recipe_name, and used_incredients_count
    recipe_id = [int(i["id"]) for i in response_list]
    # print(recipe_id)
    recipe_name =[i["title"] for i in response_list]
    # # print(recipe_name)
    used_ingredients_count = [i["usedIngredientCount"] for i in response_list]
    # # print(used_ingredients_count)
    missed_ingredients_count = [i["missedIngredientCount"] for i in response_list]
    #turning the information above to a dictionary under the recipe name key
    recipe_num_list=[]
    for num in range(5):
        r_num=f'recipe {num+1}'
        recipe_num_list.append(r_num)
    output_dict = {a:[b,c,d,e] for a,b,c,d,e in zip(recipe_num_list,recipe_name, recipe_id, used_ingredients_count, missed_ingredients_count)}
    return recipe_id

def main():
    ingredients = "chicken, celery, apple"
    ingredients = ingredients.replace(', ', '%2C+')
    num_return = 5
    ranking = 1 #1 for maximize used ingredient, 2 for minimize missing ingredients
    url = load_data(ingredients, num_return, ranking)
    data = read_data(url)
    recipe_info = lookup_recipe_id(data)
    return recipe_info

pprint.pprint(main())


