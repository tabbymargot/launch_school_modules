# Write a function that takes a string, doubles every character in the string, then returns the result as a new string.

def repeater(string):
    new_string = ""
    for letter in string:
        new_string += f'{letter}{letter}'
    return new_string



print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True