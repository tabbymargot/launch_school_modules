def leading_substrings(input_string):
    # Returns a list of all substrings within input_string starting with the first letter
    new_string = ''
    new_list = []
    for char in input_string:
        new_string += char
        new_list.append(new_string)
                        
    return new_list

def substrings(string):
    # Returns a list of all substrings within string
    substrings_list = [leading_substrings(string[idx:])
                        for idx in range(len(string))]
    
    return [substring
            for sublist in substrings_list
            for substring in sublist]

def palindromes(string):
    palindromes_list = []
    all_substrings = substrings(string)

    for substring in all_substrings:
        if (substring[::-1] == substring) and (len(substring) > 1):
            palindromes_list.append(substring)

    return palindromes_list

print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])  # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True