""" 
PROBLEM
square of the sum of the first count positive integers
- add all the integers
- square them

sum of the squares of the first count positive integers
- square the integers
- add them together

find the difference

Restate in my words
- What are the 'first count positive integers'?
- 3 = 1, 2, 3

Inputs  - integer
Outputs - integer
EXPLICIT / IMPLICIT REQUIREMENTS
- 1 returns 0

Clarifying questions
Edge cases

DATA STRUCTURES
variable to store the results of each calculation
ALGORITHM
High level - Calculate the square of the sum. Calculate the sum of the squared numbers. Calculate the difference.
Alternative High Level?
Actual algorithm
1. Calculate the square of the sum:
    - Get all the numbers up to the given integer
    - Add them together
    - Square them
    - Store the result in square_sum

2. Calculate the sum of the squared numbers.
    - Get all the numbers up to the given integer
    - Square each number
    - Add them together
    - Store the result in sum_square

3. Subtract square_sum from sum_square
"""

def sum_square_difference(n):
    numbers = list(range(1, n + 1))
    square_sum = sum(numbers)**2
    sum_square = sum([num**2 for num in numbers])
    return square_sum - sum_square

print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True