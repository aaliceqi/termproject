from flask import Flask, render_template, request
from fetch_recipe_by_id import fetch_recipe_info_by_ingredients

app = Flask(__name__)

@app.route('/')
def landingpage():
    return 'please enter "/findrecipe" to load our page'

@app.get('/findrecipe')
def findrecipe_get():
    return render_template('index.html')

@app.post('/findrecipe')
def findrecipe_post():
    ingredient = request.form.get('ingredient')
    num_return = request.form.get('num_return')
    info = fetch_recipe_info_by_ingredients(ingredient.replace(', ', '%2C+'),num_return)
    return render_template('search_page.html', recipes = info,ingredient=ingredient)    

if __name__ == '__main__':
    app.run(debug=True)