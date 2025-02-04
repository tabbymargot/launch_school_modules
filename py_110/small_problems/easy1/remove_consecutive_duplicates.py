def unique_sequence(original):
    initial_nums = []
    new_num = 0

    for num in original:
        if num != new_num:
            new_num = num
            initial_nums.append(num)

    return initial_nums 

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True