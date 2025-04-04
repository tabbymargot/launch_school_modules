# Modify your transpose function from the previous exercise so that it works with any MxN matrix with at least one row and one column.

"""  
Init a new_matrix containing the number of necessary rows. This will be equal to the number of columns in matrix.
Iterate over the matrix.
For row_index, row in matrix:
    # [1, 2, 3, 4, 5]:
    For number_index, number in row:
        # number needs to be appended to the correct index position in the correct row in new_matrix
        # Correct row will correspond to number_index - 1
        # Correct index position will correspond to row_index - 0
        # So append number to new_matrix[number_index] at position [row_index]

"""

def transpose(matrix):
    new_matrix = [[] for column in range(len(matrix[0]))]

    for row_index, row in enumerate(matrix):
        for number_index, number in enumerate(row):
            new_matrix[number_index].append(matrix[row_index][number_index])
    
    return new_matrix


print(transpose([[1, 2, 3, 4]]) == [[1], [2], [3], [4]])
print(transpose([[1], [2], [3], [4]]) == [[1, 2, 3, 4]])
print(transpose([[1]]) == [[1]])

matrix_3_by_5 = [
    [1, 2, 3, 4, 5],
    [4, 3, 2, 1, 0],
    [3, 7, 8, 6, 2],
]
expected_result = [
    [1, 4, 3],
    [2, 3, 7],
    [3, 2, 8],
    [4, 1, 6],
    [5, 0, 2],
]

print(transpose(matrix_3_by_5) == expected_result)