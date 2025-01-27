# All of these examples should print True
CONSONANTS = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

def double_consonants(string):
    new_string = ""
    # return ''.join([char * 2 for char in string if char.casefold() in CONSONANTS])
    for char in string:
        if char.casefold() in CONSONANTS:
            new_string += f'{char}{char}'
        else: 
            new_string += char

    return new_string


print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")