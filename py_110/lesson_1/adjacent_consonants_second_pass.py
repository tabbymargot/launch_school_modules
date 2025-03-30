"""  
# Given a list of strings, sort the list based on the highest number of adjacent consonants a string contains and return the sorted list. If two strings contain the same highest number of adjacent consonants, they should retain their original order in relation to each other. Consonants are considered adjacent if they are next to each other in the same word or if there is a space between two consonants in adjacent words.

PROBLEM
Inputs - list of strings
Outputs - list of sorted strings

EXPL IMPL REQ
 - Retain original order if 2 strings contain same number of adjacent consonants
 - Consonants are considered adjacent if they are next to each other in the same word or if there is a space between two consonants in adjacent words.
Clarifications
 - How do we count multiple consonants? Ie in month, how do we deal with 'nth'. Is it one instance, or multiple instances?
Edge cases

DS - dictionary to store the strings and counts

ALG
Problems
- Remove spaces inside words
- Count the number of adjacent consonants
- Sort the list of strings
HL - Get each word. Remove any spaces inside the word. Iterate through the word, counting adjacent consonants. Add word and count to dictionary. Sort the list based on the counts.
Final
Init dictionary - counts
Init vowels - 'aeiou'

For each word in the list
    Init counter to 0

    For each char in word:
        if char is alpha:
            clean_word = char
    
    for each idx, letter in clean_word:
        if idx is 0:
            if letter not in vowels, and letter at idx + 1 not in vowels
                increment counter by 1
        elif idx is equal to the length of clean_word minus 1
            if letter not in vowels, and letter at idx - 1 not in vowels
                increment counter by 1
        else
            if letter not in vowels, and letter at idx - 1 not in vowels or letter at idx + 1 not in vowels
                increment counter by 1

    append word to dictionary as key, and counter as value

    sort the list based on the values in the dictionary
"""

def sort_key(item):
    # print(item)
    return item[1]


def sort_by_consonant_count(my_list):

    counts = {}
    vowels = 'aeiou'

    for word in my_list:
        counter = 0
        clean_word = ''

        for char in word:
            if char.isalpha():
                clean_word += char
        
        for idx, letter in enumerate(clean_word):
            if (letter not in vowels):

                if idx == 0:
                    if (clean_word[idx + 1] not in vowels):
                        counter += 1

                elif idx == len(clean_word) - 1:
                    if (clean_word[idx - 1] not in vowels):
                        counter += 1

                elif (clean_word[idx + 1] not in vowels) or (clean_word[idx - 1] not in vowels):
                    counter += 1
                    
        counts[word] = counter

    lst = sorted(counts.items(), key=sort_key, reverse= True)
    return [key for key, value in lst]

# my_list = ['aa', 'baa', 'ccaa', 'dddaa']
# print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

# my_list = ['can can', 'toucan', 'batman', 'salt pan']
# print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

# my_list = ['bar', 'car', 'far', 'jar']
# print(sort_by_consonant_count(my_list))
# # ['bar', 'car', 'far', 'jar']

# my_list = ['day', 'week', 'month', 'year']
# print(sort_by_consonant_count(my_list))
# # ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']