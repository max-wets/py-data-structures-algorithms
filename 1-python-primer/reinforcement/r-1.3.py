# Write a short Python function, minmax(data), that takes a sequence of one or more numbers, and returns the smallest and largest numbers, in the form of a tuple of length two. Do not use the built-in functions min or max in implementing your solution. 
from typing import Iterable
def minmax(data: Iterable[int]) -> tuple[int, int]:
    if len(data) < 1:
        raise ValueError('The list must contain at least one element.')

    max = data[0]
    min = data[0]
    for n in data:
        if n > max:
            max = n
        if n < min:
            min = n
    return (min, max)


print(minmax([0, 12, 6, 87, 33, 4, 23, 21]))
print(minmax([7]))
print(minmax([]))