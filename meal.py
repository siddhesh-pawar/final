from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel
import requests
import json

class Meal(MethodView):
    def get(self):
        return render_template('meal.html')

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed.
        """
        # First, search the meal in the API
        api_url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={request.form['name']}"
        response = requests.get(api_url)
        data = response.json()
        
        if data['meals']:
            meal = data['meals'][0]
            # Collect ingredients
            ingredients = []
            for i in range(1, 21):  # MealDB supports up to 20 ingredients
                ingredient = meal.get(f'strIngredient{i}')
                measure = meal.get(f'strMeasure{i}')
                if ingredient and ingredient.strip():
                    if measure and measure.strip():
                        ingredients.append(f"{measure.strip()} {ingredient}")
                    else:
                        ingredients.append(ingredient)
            
            ingredients_str = ', '.join(filter(None, ingredients))
            
            model_instance = gbmodel.get_model()
            model_instance.insert_meal(
                name=meal['strMeal'],
                category=meal['strCategory'],
                area=meal['strArea'],
                instructions=meal['strInstructions'],
                ingredients=ingredients_str,
                api_id=meal['idMeal']
            )
        
        return redirect(url_for('index'))