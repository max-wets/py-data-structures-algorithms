# Write a short Python function, is_multiple(n, m), that takes two integer values 
# and returns True if n is a multiple of m, that is, n = mi for some integer i, and False otherwise.

def is_multiple(n: int, m: int):
    return True if n % m == 0 else False;

print(is_multiple(15, 3))
print(is_multiple(57, 13))