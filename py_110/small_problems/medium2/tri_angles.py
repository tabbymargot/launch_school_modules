""" 
PROBLEM
Restate in my words
Inputs 
Outputs
EXPLICIT / IMPLICIT REQUIREMENTS
Clarifying questions
Edge cases
DATA STRUCTURES
ALGORITHM
High level
Alternative High Level?
Actual algorithm
Invalid if:
    Sum is not 180
    Any angles are 0

If contains 90 - 'right'
If angle > 90 = 'obtuse'
If no angles > 89 = 'acute'

"""

def is_invalid(angles):
    if sum(angles) != 180 or 0 in angles:
        return True

def triangle(angle1, angle2, angle3):
    angles = [angle1, angle2, angle3]

    if is_invalid(angles):
        return 'invalid'
    
    if 90 in angles:
        return 'right'
    
    if any([True for angle in angles if angle > 90]):
        return 'obtuse'
    
    if all([True for angle in angles if angle < 90]):
        return 'acute'


print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True