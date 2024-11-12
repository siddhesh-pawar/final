from flask import render_template
from flask.views import MethodView
import gbmodel
import requests

class Index(MethodView):
    def get(self):
        model_instance = gbmodel.get_model()
        drinks = [dict(name=row[0], category=row[1], glass=row[2], instructions=row[3], ingredients=row[4], api_id=row[5]) 
                 for row in model_instance.select_drinks()]
        meals = [dict(name=row[0], category=row[1], area=row[2], instructions=row[3], ingredients=row[4], api_id=row[5]) 
                for row in model_instance.select_meals()]
        return render_template('index.html', drinks=drinks, meals=meals)