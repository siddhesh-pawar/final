class Model():
    def select_drinks(self):
        """
        Gets all drinks from the database
        :return: List of lists containing all rows of drinks database
        :raises: Database errors on connection and selection
        """
        pass

    def select_meals(self):
        """
        Gets all meals from the database
        :return: List of lists containing all rows of meals database
        :raises: Database errors on connection and selection
        """
        pass

    def insert_drink(self, name, category, glass, instructions, ingredients, api_id):
        """
        Inserts drink entry into database
        :param name: String
        :param category: String
        :param glass: String
        :param instructions: String
        :param ingredients: String
        :param api_id: String
        :return: True if successful
        :raises: Database errors on connection and insertion
        """
        pass

    def insert_meal(self, name, category, area, instructions, ingredients, api_id):
        """
        Inserts meal entry into database
        :param name: String
        :param category: String
        :param area: String
        :param instructions: String
        :param ingredients: String
        :param api_id: String
        :return: True if successful
        :raises: Database errors on connection and insertion
        """
        pass