WORDS_LIST = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

def associated_nums_and_words_key(associated_pair):
    integer, word = associated_pair
    return(word, integer)

def alphabetic_number_sort(input_list):
    sorted_nums_and_words = sorted(zip(input_list, WORDS_LIST), key=associated_nums_and_words_key)
    
    return [integer_and_word[0] for integer_and_word in sorted_nums_and_words]

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1, 7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)