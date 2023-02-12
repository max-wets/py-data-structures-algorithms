# Draw a class inheritance diagram for the following set of classes:

# Class Goat extends object and adds an instance variable _tail and methods milk() and jump().
# Class Pig extends object and adds an instance variable _nose and methods eat(food) and wallow().
# Class Horse extends object and adds instance variables _height and _color, and methods run() and jump().
# Class Racer extends Horse and adds a method race().
# Class Equestrian extends Horse, adding an instance variable _weight and methods trot() and is_trained().

class Goat:
    """Defines a class for goats"""

    def __init__(self, tail) -> None:
        self._tail = tail

    def milk():
        print('Got some milk...')

    def jump():
        print('Jumping around...')

class Pig:
    """Defines a class for pigs."""

    def __init__(self, nose) -> None:
        self._nose = nose

    def eat(food):
        print(f'Yummy... pigs love {food}!')

    def wallow():
        print('Oink oink!')

class Horse:
    """Defines a class for horses"""

    def __init__(self, height, color) -> None:
        self._height = height
        self._color = color

    def run():
        print('Running around in the meadows...')

    def jump():
        print('Jumping around...')

class Racer(Horse):

    def race():
        print('Dashing like a born competitor...')

class Equestrian(Horse):

    def __init__(self, height, color, weight) -> None:
        super().__init__(height, color)
        self._weight = weight

    def trot():
        print('Trotting around...')

    def is_trained():
        print('This horse has been trained.')