import requests
import json
import pprint
from config import Spoon_API
from fetch_recipe_id_by_ingredients import main
from fetch_recipe_id_by_ingredients import read_data
from fetch_recipe_id_by_ingredients import load_data
from fetch_recipe_id_by_ingredients import lookup_recipe_id

#i want to retrieve the url of the recipe using the recupe id 
APIKEY = Spoon_API
# id = 633547
id_list = main() #this contains a list of ids
# print(id_list)

def fetch_recipe_info(recipe_ids):
   
    recipe_info_list=[]
    for recipe in recipe_ids:
        id = recipe['id']
        url =f"https://api.spoonacular.com/recipes/{id}/information?apiKey={APIKEY}"
        response = (read_data(url))
        recipe_info={
            "name" : response["title"],
            "url" : response["sourceUrl"],
            "missing" : recipe["missing ingredients"],
            "not_used" : recipe["unused ingredients"]
        }
        recipe_info_list.append(recipe_info)
    return recipe_info_list

def fetch_recipe_info_by_ingredients(ingredient, num_return):
    ranking = 1
    ingredient = ingredient.replace(', ', '%2C+')
    url = load_data(ingredient, num_return, ranking)
    response = read_data(url)
    recipe_ids = lookup_recipe_id(response)
    recipe_info = fetch_recipe_info(recipe_ids)
    return recipe_info


# pprint.pprint(fetch_recipe_info_by_ingredients("chicken, celery, apple"))
# pprint.pprint(fetch_recipe_info(id_list))
#now i would like to figure out how to take the list of generated recipe ids & run it through the url to generate the corresponding url to the recipe id