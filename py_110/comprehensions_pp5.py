# Given the following data structure return a new list identical in structure to the original, but containing only the numbers that are multiples of 3.

# [[], [3, 12], [9], [15, 18]]

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

n = []

# for sublist in lst:
#     s = []
#     for num in sublist:
#         if num % 3 == 0:
#             s.append(num)
#     n.append(s)

# print(n)

def my_func(sublist):
    new = [
        num
        for num in sublist
        if num % 3 == 0
        ]

    return new

updated_list = [
    my_func(sublist)
    for sublist in lst
]

print(updated_list)