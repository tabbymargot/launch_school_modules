# Create list to store first 5 inputs.
# Get first input from user and store to the list.
# Repeat for the next 4 inputs.
# Get the 6th input and assign to a variable.
# Check whether 6th input is also in the list.
# If it is:
# Print message saying it's in the list
# If it isn't
# Print message saying it's not in the list

numbers = []
words = ('first', 'second', 'third', 'fourth', 'fifth')

for word in words:
    num = input(f'Input the {word} number\n')
    numbers.append(num)

sixth_number = input('Input the last number\n')
numbers_str = ','.join(numbers)

if sixth_number in numbers:
    print(f"{sixth_number} is in {numbers_str}'")
else: 
    print(f"{sixth_number} isn't in {numbers_str}")

print(numbers)