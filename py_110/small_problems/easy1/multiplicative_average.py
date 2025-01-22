def multiplicative_average(lst):
    running_total = 1

    for num in lst:
        running_total *= num

    divided_total = running_total / len(lst)

    integer, decimal = str(round(divided_total, 3)).split('.')
    if len(decimal) == 1:
        decimal = f'{decimal}00'
    elif len(decimal) == 2:
        decimal = f'{decimal}0'

    return f'{integer}.{decimal}'

# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")


