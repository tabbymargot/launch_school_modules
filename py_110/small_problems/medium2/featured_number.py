""" 
PROBLEM
Restate in my words
Inputs - integer
Outputs - integer
EXPLICIT / IMPLICIT REQUIREMENTS
- Must be divisible by 7
- Must be odd
- Each digit must occur only once each

Clarifying questions
Edge cases
DATA STRUCTURES
ALGORITHM
High level
Alternative High Level?
Actual algorithm

- number = integer
- if number is even, minus 1
- while True:
    - add 2 to number
    - if number % 7 != 0
        continue
    - if all digits occur only once (HELPER)
    - break
    - (otherwise continue looping)

- try / except Error

HELPER
- input is an integer
- convert each digit to strings inside a list
- create dictionary to tally occurences
- get values
- if any value is not 1, return false, otherwise true
"""
MAX_NUMBER = 9876543201

def contains_unique_digits(num):
    if len(list(str(num))) != len(set(str(num))):
        return False
    
    return True

def next_featured(number):
    if number >= MAX_NUMBER:
        return ("There is no possible number that "
                "fulfills those requirements.")
        
    if number % 2 == 0:
        number = number - 1

    while True:
        number += 2
        if number % 7 != 0:
            continue

        if contains_unique_digits(number):
            return number

print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)      # True