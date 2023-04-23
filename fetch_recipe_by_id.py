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
print(id_list)

def fetch_recipe_url(id):
    recipe_url=[]
    for id in id_list:
        url =f"https://api.spoonacular.com/recipes/{id}/information?apiKey={APIKEY}"
        response = (read_data(url))
        recipe_link = response["sourceUrl"]
        recipe_url.append((id, recipe_link))
    return recipe_url   

def fetch_recipe_url_by_ingredients(ingredient):
    num_return = 5
    ranking = 1
    url = load_data(ingredient, num_return, ranking)
    response = read_data(url)
    id = lookup_recipe_id(response)
    recipe_url = lookup_recipe_id(id)
    return recipe_url

print(fetch_recipe_url(id_list))
#now i would like to figure out how to take the list of generated recipe ids & run it through the url to generate the corresponding url to the recipe id