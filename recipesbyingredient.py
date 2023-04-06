url = "https://api.spoonacular.com/recipes/findByIngredients"

f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
pprint.pprint(response_data)