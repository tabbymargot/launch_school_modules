CONSONANTS = "bcdfghjklmnpqrstvwxyz"

def sort_by_consonant_count(lst):
    
    words_and_scores = []
    sorted_words = []

    for word in lst:
        points_running_total = 0
        word = word.replace(" ", "")

        for idx, current_letter in enumerate(word):

            if idx != len(word) - 1:
                next_letter = word[idx + 1]
            if idx != 0:
                previous_letter = word[idx - 1]

            if current_letter in CONSONANTS:
                # If it's the first letter in the string and the next letter is a consonant
                if idx == 0:
                    # print(current_letter)
                    if next_letter in CONSONANTS:
                        points_running_total += 1
                        # print(points_running_total)
                # If it's the last letter in the string and the previous letter is a consonant
                elif idx == len(word) - 1:
                    # print(current_letter)
                    if previous_letter in CONSONANTS:
                        points_running_total += 1
                        # print(points_running_total)
                # If it's any other letter in the string and the previous and / or next letter is a consonant
                else:
                    # print(current_letter)
                    if (previous_letter in CONSONANTS) or (next_letter in CONSONANTS):
                        points_running_total += 1
                        # print(points_running_total)
        word_and_score = [word, points_running_total]  
        # print(word_and_score)    
        words_and_scores.append(word_and_score)
    
    return words_and_scores 


# my_list = ['bbaa', 'ccaa']
# print(sort_by_consonant_count(my_list))

# my_list = ['aa', 'baa', 'ccaa', 'dddaa']
# print(sort_by_consonant_count(my_list))
# # ['dddaa', 'ccaa', 'aa', 'baa']

# my_list = ['can can', 'toucan', 'batman', 'salt pan']
# print(sort_by_consonant_count(my_list))
# # ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# # ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# # ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# # ['xxxx', 'xxxb', 'xxxa']