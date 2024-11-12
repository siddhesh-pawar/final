from flask import Flask
from flask.views import MethodView
from index import Index
from drink import Drink
from meal import Meal
import gbmodel

app = Flask(__name__)

app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])

app.add_url_rule('/drink/',
                 view_func=Drink.as_view('drink'),
                 methods=['GET', 'POST'])

app.add_url_rule('/meal/',
                 view_func=Meal.as_view('meal'),
                 methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)