"""  
PROBLEM
Write a function that takes a year as an argument and returns the number of Friday the 13ths in that year. You may assume that the year is greater than 1752.

Restate in my words
Inputs - integer (year)
Outputs - integer
EXPLICIT / IMPLICIT REQUIREMENTS
- year will be greater than 1752

Clarifying questions
Edge cases
DATA STRUCTURES
Dictionary number_of_fridays?
List?
ALGORITHM
High level
Get the year. Find out how many times the 13th fell on a Friday in that year. Return the count.
Alternative High Level?
Actual algorithm
- init counter
- Pass year into date as first variable
- Set 3rd date variable to 13
- Create range 1 - 12, representing months
    - for each month, pass month into date as 2nd variable
    - Get the day of the week for the 13th - will be an integer
    - If the integer is 5, that's a Friday. Increment the counter.
Return the counter

"""
from datetime import date

def friday_the_13ths(year):
    months_list = [num for num in range(1, 13)]
    number_of_fridays = 0

    for month in months_list:
        day_of_week = date(year, month , 13).isoweekday()
        if day_of_week == 5:
            number_of_fridays += 1

    return number_of_fridays

print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True