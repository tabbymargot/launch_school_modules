CONSONANTS = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

# SOLUTION 1
def remove_vowels(original):
    new_list = []

    for string in original:
        consonant_string = ""
        for char in string:
            if char in CONSONANTS:
                consonant_string += char
        new_list.append(consonant_string)
    
    return new_list


# SOLUTION 2
# def remove_vowels(original):
#     for string in original:
#         consonant_string_list = [
#             char
#             for char in string
#             if char in CONSONANTS
#         ]
#         new_list.append(''.join(consonant_string_list))

#     return new_list



# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True