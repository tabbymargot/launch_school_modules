def leading_substrings(input_string):
    new_string = ''
    new_list = []
    for char in input_string:
        new_string += char
        new_list.append(new_string)
                        
    return new_list

def substrings(string):
    substrings_list = [leading_substrings(string[idx:])
                        for idx in range(len(string))]
    
    return [substring
            for sublist in substrings_list
            for substring in sublist]

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True