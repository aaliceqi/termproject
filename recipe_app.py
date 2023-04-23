from flask import Flask, render_template, request
from fetch_recipe_by_id import fetch_recipe_url_by_ingredients

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
    url = fetch_recipe_url_by_ingredients(ingredient.replace(', ', '%2C+'))
    return render_template('result.html', recipe_url = url)    

if __name__ == '__main__':
    app.run(debug=True)