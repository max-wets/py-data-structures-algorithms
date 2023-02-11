# Python allows negative integers to be used as indices into a sequence, such as a string. If string s has length n, and expression s[k] is used for index −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references the same element?
def reverse_index(idx: int, len: int) -> int:
    return len - abs(idx) if idx < 0 else 0

list = [0, 12, 8, 46, 8, 20, 56, 78]

for k in range(-len(list), 0):
    print(list[k] == list[reverse_index(k, len(list))])