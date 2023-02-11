# Write a short Python function, is_even(k), that takes an integer value and returns True if k is even, and False otherwise. However, your function cannot use the multiplication, modulo, or division operators.
def is_even(k: int):
    last_even = 0
    while (last_even < k):
        last_even += 2
    return last_even == k

print(is_even(13))