# Write a short Python function that takes a positive integer n and returns the sum of the squares of all the positive integers smaller than n.
def sq_sum(n: int) -> int:
    return sum([x**2 for x in range(0, n)])

print(sq_sum(6))