def leading_substrings(input_string):
    new_string = ''
    new_list = []
    for char in input_string:
        new_string += char
        new_list.append(new_string)
                        
    return new_list

# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])