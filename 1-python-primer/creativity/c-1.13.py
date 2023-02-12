# Write a pseudo-code description of a function that reverses a list of n integers, so that the numbers are listed in the opposite order than they were before, and compare this method to an equivalent Python function for doing the same thing.
from typing import Iterable

def my_reverse(data: Iterable[int]) -> list[int]:
    reversed_list = []
    for i in range(len(data) - 1, -1, -1):
        reversed_list.append(data[i])
    return reversed_list

list1 = [0, 23, 66, 87, 12, 14, 93, 56, 34, 8]
print(my_reverse(list1))
print(list(reversed(list1)))