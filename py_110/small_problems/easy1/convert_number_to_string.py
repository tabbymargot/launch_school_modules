INTEGER_KEYS = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
}

def integer_to_string(number):
    DIVISOR = 10
    num_string = ""

    while True:
        number, remainder = divmod(number, DIVISOR)
        remainder_string = INTEGER_KEYS[remainder]
        num_string = f'{remainder_string}{num_string}'
        if number == 0:
            break

    return num_string

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True