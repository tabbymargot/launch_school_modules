def swap(string):
    modified_words = []
    original_string_as_list = string.split()

    for word in original_string_as_list:
        first_char = ''
        last_char = ''
        list_of_chars = list(word)

        first_char = list_of_chars.pop(0)

        if len(list_of_chars) > 0:
            last_char = list_of_chars.pop(-1)

        list_of_chars.insert(0, last_char)
        list_of_chars.append(first_char)

        modified_words.append(''.join(list_of_chars))
    
    return ' '.join(modified_words)
        

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True