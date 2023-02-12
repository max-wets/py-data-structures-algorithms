# Write a Python class, Flower, that has three instance variables of type str, int, and float, that respectively represent the name of the flower, its number of petals, and its price. Your class must include a constructor method that initializes each variable to an appropriate value, and your class should include methods for setting the value of each type, and retrieving the value of each type. 

class Flower:
    """A simple Flower class
    
    name    the name of the flower (e.g. 'Rose')
    petals  the number of petals (e.g. '12')
    price   the price of the flower (e.g. '1.23')
    """

    def __init__(self, name: str, petals: int, price: float) -> None:
        self.name = name
        self.petals = petals
        self.price = price

    def get_name(self):
        """Returns name of the flower"""
        return self.name
    def set_name(self, value):
        """Sets name of the flower"""
        self.name = value

    def get_petals(self):
        """Returns number of petals of the flower"""
        return self.petals
    def set_petals(self, value):
        """Sets number of petals of the flower"""
        self.petals = value

    def get_price(self):
        """Returns the price of the flower"""
        return self.price
    def set_price(self, value):
        """Sets price of the flower"""
        self.price = value

    

rose = Flower('Rose', 8, 1.23)
print(rose.get_name())
rose.set_name('Begonia')
print(rose.get_name())