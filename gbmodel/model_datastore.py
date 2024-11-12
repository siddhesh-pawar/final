from .Model import Model
from google.cloud import datastore

def from_datastore_drink(entity):
    """Translates Datastore results into the format expected by the application."""
    if not entity:
        return None
    if isinstance(entity, list):
        entity = entity.pop()
    return [
        entity['name'],
        entity['category'],
        entity['glass'],
        entity['instructions'],
        entity['ingredients'],
        entity['api_id']
    ]

def from_datastore_meal(entity):
    """Translates Datastore results into the format expected by the application."""
    if not entity:
        return None
    if isinstance(entity, list):
        entity = entity.pop()
    return [
        entity['name'],
        entity['category'],
        entity['area'],
        entity['instructions'],
        entity['ingredients'],
        entity['api_id']
    ]

class model(Model):
    def __init__(self):
        self.client = datastore.Client('cloud-pawar-sidpawar')  # Replace with your project ID

    def select_drinks(self):
        query = self.client.query(kind='Drinks')
        entities = list(map(from_datastore_drink, query.fetch()))
        return entities

    def select_meals(self):
        query = self.client.query(kind='Meals')
        entities = list(map(from_datastore_meal, query.fetch()))
        return entities

    def insert_drink(self, name, category, glass, instructions, ingredients, api_id):
        key = self.client.key('Drinks', api_id)  # Using api_id as the key
        drink = datastore.Entity(key)
        drink.update({
            'name': name,
            'category': category,
            'glass': glass,
            'instructions': instructions,
            'ingredients': ingredients,
            'api_id': api_id
        })
        self.client.put(drink)
        return True

    def insert_meal(self, name, category, area, instructions, ingredients, api_id):
        key = self.client.key('Meals', api_id)  # Using api_id as the key
        meal = datastore.Entity(key)
        meal.update({
            'name': name,
            'category': category,
            'area': area,
            'instructions': instructions,
            'ingredients': ingredients,
            'api_id': api_id
        })
        self.client.put(meal)
        return True