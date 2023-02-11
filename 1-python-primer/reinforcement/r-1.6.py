# Write a short Python function that takes a positive integer n and returns the sum of the squares of all the odd positive integers smaller than n.
def odd_sq_sum(n: int) -> int:
    return sum([x**2 for x in range(n) if x % 2 != 0])

print(odd_sq_sum(3))