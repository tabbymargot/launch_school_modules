INTEGER_KEYS = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
}

LEADING_SIGNS = {'+', '-'}

def string_to_signed_integer(num_string):
    multiplier = 1
    running_total = 0
    leading_sign = ""

    if num_string[0] in LEADING_SIGNS:
        leading_sign = num_string[0]
        num_string = num_string[1:]

    for str_num in reversed(list(num_string)):
        current_integer = INTEGER_KEYS[str_num]
        running_total += current_integer * multiplier
        multiplier *= 10
    
    if leading_sign == "-":
        running_total = 0 - running_total

    return running_total


print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True