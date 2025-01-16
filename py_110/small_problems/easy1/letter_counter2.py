def clean_words(word_list):
    clean_word_list = []

    for word in word_list:
        clean_word = ""
        for char in word:
            if char.isalpha():
                clean_word += char

        clean_word_list.append(clean_word)

    return clean_word_list


def word_sizes(string):
    word_list = string.split()
    clean_word_list = clean_words(word_list)

    word_lengths = {}

    for word in clean_word_list: 
        number_of_chars = len(word)
        word_lengths.setdefault(number_of_chars, 0)
        word_lengths[number_of_chars] += 1

    return word_lengths


# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})