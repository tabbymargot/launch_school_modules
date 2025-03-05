"""  
PROBLEM
Create a dictionary as follows:
'lowercase': the percentage of characters that are lowercase letters
'uppercase: the percentage of characters that are uppercase letters
'neither': the percentage of characters that are neither


Restate in my words
Inputs 
String

Outputs
Dictionary

EXPLICIT / IMPLICIT REQUIREMENTS
- a space counts as a character


Clarifying questions
Edge cases

DATA STRUCTURES
- Dictionary to store the count of each type of char
ALGORITHM
High level - Count the number of each type of char in the string. Calculate the percentages based on those counts and the length of the string. Assign the results to a dictionary.

Actual algorithm
- Get the length of the string (= total chars) - assign to var total_chars
HELPER FUNC - count_the_chars
    - Create an empty dictionary char_counts
    - Loop through the chars in the string.
        If the char is lowercase:
            Create key 'lowercase' and assoc value 1, or increment value by 1 if key already exists.
        If uppercase:
            Create key 'uppercase' and assoc value 1, or increment value by 1 if key already exists.
        If neither:
            Create key 'neither' and assoc value 1, or increment value by 1 if key already exists.
        
    - Return the dictionary

HELPER FUNC - calculate percentages
    - Pass in char_counts, total_chars
    - Init new dictionary percentages
    - Loop over char_counts - get the key (letter_type) and the value (char_count)
        - Create new value called percentage - char_count / total_chars * 100. Round it to 2 decimal points.
        - Set percentages[letter_type] to percentage

    Return the dictionary

Return the dictionary

"""
def count_the_chars(string):
    char_counts = {
        'lowercase': 0,
        'uppercase': 0,
        'neither': 0,
    }
    
    for char in string:
        if char.islower():
            char_counts['lowercase'] = char_counts['lowercase'] + 1
        elif char.isupper():
            char_counts['uppercase'] = char_counts['uppercase'] + 1
        else:
            char_counts['neither'] = char_counts['neither'] + 1
            
    return char_counts


def calculate_percentages(char_counts, total_chars):
    percentages = {}
    for letter_type, char_count in char_counts.items():
        percentage = (char_count / total_chars) * 100
        percentages[letter_type] = f'{percentage}0'

    return percentages


def letter_percentages(string):
    total_chars = len(string)
    char_counts = count_the_chars(string)
    percentages = calculate_percentages(char_counts, total_chars)
    return percentages

expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)