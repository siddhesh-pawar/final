from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel
import requests
import json

class Drink(MethodView):
    def get(self):
        return render_template('drink.html')

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed.
        """
        # First, search the cocktail in the API
        api_url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={request.form['name']}"
        response = requests.get(api_url)
        data = response.json()
        
        if data['drinks']:
            drink = data['drinks'][0]
            # Collect ingredients
            ingredients = []
            for i in range(1, 16):  # CocktailDB supports up to 15 ingredients
                ingredient = drink.get(f'strIngredient{i}')
                measure = drink.get(f'strMeasure{i}')
                if ingredient:
                    if measure:
                        ingredients.append(f"{measure.strip()} {ingredient}")
                    else:
                        ingredients.append(ingredient)
            
            ingredients_str = ', '.join(filter(None, ingredients))
            
            model_instance = gbmodel.get_model()
            model_instance.insert_drink(
                name=drink['strDrink'],
                category=drink['strCategory'],
                glass=drink['strGlass'],
                instructions=drink['strInstructions'],
                ingredients=ingredients_str,
                api_id=drink['idDrink']
            )
        
        return redirect(url_for('index'))
