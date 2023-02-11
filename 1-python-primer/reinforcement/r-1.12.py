# Python's random module includes a function choice(data) that returns a random element from a non-empty sequence. The random module includes a more basic function randrange, with parameterization similar to the built-in range function, that return a random choice from the given range. Using only the randrange function, implement your own version of the choice function. 
from random import randrange
from typing import Iterable, Any

def choice(data: Iterable[Any]) -> Any:
    return data[randrange(len(data))]

list1 = ["abc", "bca", "cba", "acb", "bac", "cab"]
print(choice(list1))