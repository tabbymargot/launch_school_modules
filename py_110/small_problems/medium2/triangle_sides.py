# To be a valid triangle, the sum of the lengths of the two shortest sides must be greater than the length of the longest side, 
# and every side must have a length greater than 0. If either of these conditions is not satisfied, the triangle is invalid.

"""  
- pop the max number
- if the sum of the remaining numbers is less than than the popped number, return invalid

if any of the integers == 0, return invalid


create set containing the integers.
- if set contains 2 integer, return "equilateral"
- if set contains 1 integer, return ""isosceles""
- if set contains 3 integers, return "scalene"

"""

def is_invalid(sides):
    if 0 in sides:
        return True
    
    sides.sort()
    if (sides[0] + sides[1]) <= sides[2]:
        return True

def triangle(side1, side2, side3):
    sides = [side1, side2, side3]
    if is_invalid(sides):
        return 'invalid'
    
    match len(set(sides)):
        case 1: 
            return "equilateral"
        case 2:
            return "isosceles"
        case 3: 
            return "scalene"
    

# print(triangle(3, 3, 3) == "equilateral")  # True
# print(triangle(3, 3, 1.5) == "isosceles")  # True
# print(triangle(3, 4, 5) == "scalene")      # True
# print(triangle(0, 3, 3) == "invalid")      # True
# print(triangle(3, 1, 1) == "invalid")      # True

print(triangle(1, 2, 3)) 


