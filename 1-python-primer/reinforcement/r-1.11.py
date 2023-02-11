## Demonstrate how to use Python's list comprehension syntax to produce the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
# traditional for loop
list1 = []
for i in range(9):
    if i > 0:
        list1.append(list1[i-1] * 2)
    else:
        list1.append(1)

# with list comprehension
list2 = [ 2**i for i in range(9) ]

print(list1)
print(list2)
