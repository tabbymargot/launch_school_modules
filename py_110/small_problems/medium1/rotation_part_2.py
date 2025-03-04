# Write a function that rotates the last count digits of a number. To perform the rotation, move the first of the digits that you want to rotate to the end and shift the remaining digits to the left.

"""  
P: Get the digit that's at the negative index position indicated by the second argument. Move that digit to the end of the integer. Any digits to its right will shift to the left.

Input - integer
Output - integer

Requirements:
- If the digit is already at the end, leave it there.
- The number of digits in the integer doesn't matter - should work the same for all.

Edge cases:

DS:
string - so that digits can be separated
list - so they can be reordered
string - before converting back into an integer

HL:
Locate and select the digit to be moved. Reposition it at the end of the string. If not done automatically, reposition the digits that were to its right.

Alternative?:
Locate and select the digits to the right and move those instead - this looks harder.

Algorithm:
- Init integer_str.
- Init digits_lst
- Transform integer to string and assign to integer_str
- Transform string to list and assign to digits_lst
- Access the digit to be moved by its negative index and assign to single_digit. Use remove to do this?
- Append single_digit to end of digits_lst.
- Convert digits_list back to string, and then back to integer
- Return
"""
def rotate_rightmost_digits(number, idx):
    digits_lst = list(str(number))
    single_digit = digits_lst.pop(-idx)
    digits_lst.append(single_digit)
    return int(''.join(digits_lst))

print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True