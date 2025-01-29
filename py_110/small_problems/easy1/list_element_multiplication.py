def multiply_items(list_a, list_b):
    return [a * b for a, b in zip(list_a, list_b)]

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True