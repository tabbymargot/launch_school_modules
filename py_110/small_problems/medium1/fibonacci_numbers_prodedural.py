# The Fibonacci series is a sequence of numbers in which each number is the sum of the previous two numbers. 
# The first two Fibonacci numbers are 1 and 1. 
# The third number is 1 + 1 = 2, the fourth is 1 + 2 = 3, the fifth is 2 + 3 = 5, the sixth is 3 + 5 = 8, and so on. 
# In mathematical terms, this can be represented as:

# F(1) = 1
# F(2) = 1
# F(n) = F(n - 1) + F(n - 2)    (where n > 2)

"""  
PROBLEM
Restate in my words
The argument passed to a function will be the position of nth number in the Fibonacci sequence. Calculate what that number is.

Inputs 
Integer

Outputs
Integer

EXPLICIT / IMPLICIT REQUIREMENTS

- The input will always be a positive integer
- If the input is less than 3 (ie 1), may need a special action to be taken

Clarifying questions
Edge cases

DATA STRUCTURES
- List to hold the values?
ALGORITHM

High level - If n is less than 3, return 1. Otherwise, calculate the Fibonacci number.

def fibonacci(n):
    # Handle base cases
    if n <= 2:
        return 1
    
    # Initialize the first two Fibonacci numbers
    # Then use a loop to calculate each subsequent number
    # until you reach the nth
    
    # Return the nth number

Alternative High Level?
Actual algorithm
"""

""" 
Sequence: 1, 1, 2, 3, 5, 8

Anchor is the last index position that we want to access.

- F3
    - Add the numbers at indexes 0 (1) + 1 (1), and append result to list (2)
        [1, 1, 2]
    - Anchor = 1 (3 - 2)
- F4
    - Add the numbers at indexes 0 (1) + 1 (1), and append result to list (2)
    - Add the numbers at indexes 1 (1) + 2 (2), and append result to list (3)
        [1, 1, 2, 3]
    - Anchor = 2 (4 - 2)
- F5
    - Add the numbers at indexes 0 (1) + 1 (1), and append result to list (2)
    - Add the numbers at indexes 1 (1) + 2 (2), and append result to list (3)
    - Add the numbers at indexes 2 (2) + 3 (3), and append result to list (5)
        [1, 1, 2, 3, 5]
    - Anchor = 3 (5 - 2)
- F6
    - Add the numbers at indexes 0 (1) + 1 (1), and append result to list (2)
    - Add the numbers at indexes 1 (1) + 2 (2), and append result to list (3)
    - Add the numbers at indexes 2 (2) + 3 (3), and append result to list (5)
    - Add the numbers at indexes 3 (3) + 4 (5), and append result to list (8)
        [1, 1, 2, 3, 5, 8] 
    - Anchor = 4 (6 - 2)
"""

def fibonacci(num):
    fib_list = [1, 1]
    anchor = num - 2 
    for idx in range(anchor): 
        fib_list.append(fib_list[idx]+ fib_list[idx + 1])
    
    return fib_list[-1]


print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True