# Write a recursive function that computes the nth Fibonacci number, where nth is an argument passed to the function.

# F(1) = 1
# F(2) = 1
# F(n) = F(n - 1) + F(n - 2)    (where n > 2)

"""  
PROBLEM
Restate in my words
Inputs - integer
Outputs - interger
EXPLICIT / IMPLICIT REQUIREMENTS
- use a recursive function
Clarifying questions
Edge cases
DATA STRUCTURES
ALGORITHM
High level
Alternative High Level?
Actual algorithm

If fibnum == 1 or 2, return 1

fib_list = [1, 1]

fibnum == 5
anchor = 0

If the length of fib_list is less than fibnum: # 4
    append (fib_list[anchor] + fib_list[anchor + 1]) to fib_list # fib_list = [1, 1, 2, 3, 5]
    if fibnum > len(fib_list)
        anchor += 1 # 2
        fib_recursive(fibnum)
    else
        return fib_list[-1]
"""

fib_list = [1, 1]

def fibonacci(fibnum):
    if fibnum == 1 or fibnum == 2:
        return 1

    fib_list.append(fib_list[len(fib_list) - 2] + fib_list[len(fib_list) - 1])

    if fibnum > len(fib_list):
        fibonacci(fibnum)

    return fib_list[-1]

print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True