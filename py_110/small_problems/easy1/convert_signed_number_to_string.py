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

    while number > 0:
        number, remainder = divmod(number, DIVISOR)
        remainder_string = INTEGER_KEYS[remainder]
        num_string = f'{remainder_string}{num_string}'

    return num_string

def signed_integer_to_string(num):
    if num < 0:
        num = num * -1
        number_string = f'-{integer_to_string(num)}'
    elif num > 0:
        number_string = f'+{integer_to_string(num)}'
    else: 
        number_string = f'{integer_to_string(num)}'
    return number_string

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True