# Write a function that takes a string as an argument and returns that string with every occurrence of a "number word" -- 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' -- converted to its corresponding digit character.

# You may assume that the string does not contain any punctuation.

"""  
PROBLEM
- Restate in my words
    Transform a string so that all 'number words' are replaced with an actual digit.
Inputs - string
Outputs - string


EXPLICIT / IMPLICIT REQUIREMENTS
- No punctuation
- all lower case
- repeated words will have repeated digits

Clarifying questions
Edge cases
DATA STRUCTURES
- List of word strings
- Dictionary to convert words to digits

ALGORITHM
High level
Create a dictionary with number words as keys, and digits as values. For each number word in the string, get the key from the dictionary and replace it with the value.

Alternative High Level?

Actual algorithm
- Create a new_list to hold the original and transformed substrings
- Create a dictionary with number words as keys, and digits as values.
- Convert the string to a list of substrings, with each word being a substring.
- Iterate over the list. For each word:
    - Check whether it matches a key in the dictionary.
    - If it does:
        - Get the value and append it to new_list
    - If it doesn't:
        - Append the original substring to new_list.
- Join all the substrings in new_list back into a string.
- Return the string

"""

TABLE = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
}
# print(TABLE)

def word_to_digit(string):
    new_list = []
    list_of_substrings = string.split()
    for word in list_of_substrings:
        if word in TABLE:
            new_list.append(TABLE[word])
        else:
            new_list.append(word)
    return ' '.join(new_list)

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True