def word_sizes(string):
    word_list = string.split()
    word_lengths = {}

    for word in word_list: 
        number_of_chars = len(word)
        word_lengths.setdefault(number_of_chars, 0)
        word_lengths[number_of_chars] += 1

    return word_lengths



# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})