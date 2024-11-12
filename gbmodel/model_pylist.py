from .Model import Model

class model(Model):
    def __init__(self):
        self.drinks = []
        self.meals = []

    def select_drinks(self):
        return [[
            drink['name'],
            drink['category'],
            drink['glass'],
            drink['instructions'],
            drink['ingredients'],
            drink['api_id']
        ] for drink in self.drinks]

    def select_meals(self):
        return [[
            meal['name'],
            meal['category'],
            meal['area'],
            meal['instructions'],
            meal['ingredients'],
            meal['api_id']
        ] for meal in self.meals]

    def insert_drink(self, name, category, glass, instructions, ingredients, api_id):
        drink = {
            'name': name,
            'category': category,
            'glass': glass,
            'instructions': instructions,
            'ingredients': ingredients,
            'api_id': api_id
        }
        # Update existing drink if api_id exists
        for i, existing_drink in enumerate(self.drinks):
            if existing_drink['api_id'] == api_id:
                self.drinks[i] = drink
                return True
        self.drinks.append(drink)
        return True

    def insert_meal(self, name, category, area, instructions, ingredients, api_id):
        meal = {
            'name': name,
            'category': category,
            'area': area,
            'instructions': instructions,
            'ingredients': ingredients,
            'api_id': api_id
        }
        # Update existing meal if api_id exists
        for i, existing_meal in enumerate(self.meals):
            if existing_meal['api_id'] == api_id:
                self.meals[i] = meal
                return True
        self.meals.append(meal)
        return True