def sequence(int1, int2):
    num_list = list(range(1, int1 + 1))
    return [num * int2 for num in num_list]



print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True