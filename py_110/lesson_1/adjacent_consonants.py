# PEDAC outline is here: capacities://f3ac60b1-b034-4dd7-b4d7-629caa9a67bf/4c547bac-9525-43ae-a20a-d0bb5c86ff0a

CONSONANTS = "bcdfghjklmnpqrstvwxyz"

def sort_by_consonant_count(lst):
    
    words_and_scores = []
    sorted_words = []

    for word in lst:
        points_running_total = 0
        word_no_space = word.replace(" ", "")

        for idx, current_letter in enumerate(word_no_space):

            if idx != len(word_no_space) - 1:
                next_letter = word_no_space[idx + 1]
            if idx != 0:
                previous_letter = word_no_space[idx - 1]

            if current_letter in CONSONANTS:
                # If it's the first letter in the string and the next letter is a consonant
                if idx == 0:
                    if next_letter in CONSONANTS:
                        points_running_total += 1
                # If it's the last letter in the string and the previous letter is a consonant
                elif idx == len(word_no_space) - 1:
                    if previous_letter in CONSONANTS:
                        points_running_total += 1
                # If it's any other letter in the string and the previous and / or next letter is a consonant
                else:
                    if (previous_letter in CONSONANTS) or (next_letter in CONSONANTS):
                        points_running_total += 1
        
        word_and_score = [word, points_running_total]  
        words_and_scores.append(word_and_score)
    
    list_of_sorted_words = sort_the_words(words_and_scores)
    return list_of_sorted_words

def sort_the_words(the_words_and_scores):
    scores = []
    sorted_words = []

    for nested_list in the_words_and_scores:
        scores.append(nested_list[1])

    score_being_checked = max(scores)

    while score_being_checked >= 0:
        for the_nested_list in the_words_and_scores:
            if the_nested_list[1] == score_being_checked:
                sorted_words.append(the_nested_list[0])

        score_being_checked -= 1

    return sorted_words

# my_list = ['aa', 'baa', 'ccaa', 'dddaa']
# print(sort_by_consonant_count(my_list))
# # # ['dddaa', 'ccaa', 'aa', 'baa']

# my_list = ['can can', 'toucan', 'batman', 'salt pan']
# print(sort_by_consonant_count(my_list))
# # # ['salt pan', 'can can', 'batman', 'toucan']

# my_list = ['bar', 'car', 'far', 'jar']
# print(sort_by_consonant_count(my_list))
# # # # ['bar', 'car', 'far', 'jar']

# my_list = ['day', 'week', 'month', 'year']
# print(sort_by_consonant_count(my_list))
# # # # ['month', 'day', 'week', 'year']

my_list = ['xxaxxaxxaxxaxxa', 'xxxx', 'xxxb', 'rstafgdjecc']
print(sort_by_consonant_count(my_list))
# # ['xxxx', 'xxxb', 'xxxa']