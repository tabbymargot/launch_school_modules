CONSONANTS = "bcdfghjklmnpqrstvwxyz"

def sort_by_consonant_count(lst):
    points_running_total = 0
    store_nested_lists = []
    sorted_words = []

    for word in lst:
        word = word.replace(" ", "")
        letters_list = list(word)
        for idx, current_letter in enumerate(letters_list):
            if current_letter in CONSONANTS:
                if idx == 0:
                    print(current_letter)
                    if letters_list[idx + 1] in CONSONANTS:
                        points_running_total += 1
                        print(points_running_total)
                elif idx == -1:
                    print(current_letter)
                    if letters_list[idx - 1] in CONSONANTS:
                        points_running_total += 1
                        print(points_running_total)
                else:
                    print(current_letter)
                    if (letters_list[idx - 1] in CONSONANTS) or (letters_list[idx + 1] in CONSONANTS):
                        points_running_total += 1
                        print(points_running_total)

my_list = ['da mn']
print(sort_by_consonant_count(my_list))

# my_list = ['aa', 'baa', 'ccaa', 'dddaa']
# print(sort_by_consonant_count(my_list))
# # ['dddaa', 'ccaa', 'aa', 'baa']

# my_list = ['can can', 'toucan', 'batman', 'salt pan']
# print(sort_by_consonant_count(my_list))
# # ['salt pan', 'can can', 'batman', 'toucan']

# my_list = ['bar', 'car', 'far', 'jar']
# print(sort_by_consonant_count(my_list))
# # ['bar', 'car', 'far', 'jar']

# my_list = ['day', 'week', 'month', 'year']
# print(sort_by_consonant_count(my_list))
# # ['month', 'day', 'week', 'year']

# my_list = ['xxxa', 'xxxx', 'xxxb']
# print(sort_by_consonant_count(my_list))
# # ['xxxx', 'xxxb', 'xxxa']