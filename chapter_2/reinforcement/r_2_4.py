class Flower:
    """
    name        string with name of flower
    petals  int with number of petals
    price       float with price of flower
    """

    def __init__(self, name, petals, price):
        self._name = name
        self._petals = petals
        self._price = price

    def get_name(self):
        return self._name
    
    def get_petals(self):
        return self._petals
    
    def get_price(self):
        return self._price

    def set_name(self, new_name):
        self._name = new_name
    
    def set_petals(self, new_petals):
        self._petals = new_petals

    def set_price(self, new_price):
        self._price = new_price
