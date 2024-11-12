from datetime import date
from .Model import Model
import sqlite3

DB_FILE = 'fooddrink.db'

class model(Model):
    def __init__(self):
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from drinks")
            cursor.execute("select count(rowid) from meals")
        except sqlite3.OperationalError:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS drinks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    category TEXT,
                    glass TEXT,
                    instructions TEXT,
                    ingredients TEXT,
                    api_id TEXT UNIQUE
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS meals (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    category TEXT,
                    area TEXT,
                    instructions TEXT,
                    ingredients TEXT,
                    api_id TEXT UNIQUE
                )
            ''')
        cursor.close()
        connection.close()

    def select_drinks(self):
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT name, category, glass, instructions, ingredients, api_id FROM drinks")
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        return results

    def select_meals(self):
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT name, category, area, instructions, ingredients, api_id FROM meals")
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        return results

    def insert_drink(self, name, category, glass, instructions, ingredients, api_id):
        params = {
            'name': name,
            'category': category,
            'glass': glass,
            'instructions': instructions,
            'ingredients': ingredients,
            'api_id': api_id
        }
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO drinks 
            (name, category, glass, instructions, ingredients, api_id) 
            VALUES (:name, :category, :glass, :instructions, :ingredients, :api_id)
        """, params)
        connection.commit()
        cursor.close()
        connection.close()
        return True

    def insert_meal(self, name, category, area, instructions, ingredients, api_id):
        params = {
            'name': name,
            'category': category,
            'area': area,
            'instructions': instructions,
            'ingredients': ingredients,
            'api_id': api_id
        }
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO meals 
            (name, category, area, instructions, ingredients, api_id) 
            VALUES (:name, :category, :area, :instructions, :ingredients, :api_id)
        """, params)
        connection.commit()
        cursor.close()
        connection.close()
        return True