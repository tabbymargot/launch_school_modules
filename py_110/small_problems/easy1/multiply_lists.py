def multiply_list(list1, list2):
    products = []

    for num1, num2 in zip(list1, list2):
        products.append(num1 * num2)

    return products


list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True