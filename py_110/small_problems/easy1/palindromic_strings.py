def is_palindrome(string):
    if len(string) % 2 == 0:
        half_length = len(string) // 2
    else:
        half_length = (len(string) // 2) + 1

    left_counter = 0
    right_counter = -1

    while left_counter < half_length:
        left_char = string[left_counter]
        right_char = string[right_counter]
        if left_char != right_char:
            return False
        left_counter += 1
        right_counter -= 1

    return True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)
