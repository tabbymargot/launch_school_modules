integer = int(input('Please enter an integer greater than 0: '))

operation_type = input('''
Enter "s" to compute the sum, 
or "p" to compute the product.
'''                  
)

def get_sum(number):
    running_total = number
    for num in range(number-1, 0, -1):
        running_total += num

    return running_total

def get_product(number):
    running_total = number
    for num in range(number-1, 1, -1):
        running_total *= num

    return running_total

if operation_type == 's':
    result = get_sum(integer)
    print(f'The sum of the integers between 1 and {integer} is {result}.')
elif operation_type == 'p':
    result = get_product(integer)
    print(f'The product of the integers between 1 and {integer} is {result}.')