"""
PROBLEM
- Restate in my words:
735291
To get this 352917 - Move the first digit to the end
To get this 329175 - Move the second digit to the end
321759 - Move the third digit to the end
321597 - Move the 4th digit to the end
321579 - Move the 5th digit to the end

Inputs - Integer
Outputs - Integer

EXPLICIT / IMPLICIT REQUIREMENTS

- Should work with strings of any length
- There will always be at least one digit in the integer
- Any leading 0 will be dropped on a final integer

Clarifying questions
Edge cases

DATA STRUCTURES
string
list - to reorder the chars in the string

ALGORITHM
High level
In turn, move the first, second, third etc integers until the end. Note - we'll be mutating the list as we go, so proceed with caution.

Alternative High Level?

Actual algorithm
- Coerce the integer to a string, then to a list. Assign to digits_list
- Iterate over the list. Starting at index 0, remove the char and append to the end of the list (use pop?)
    - Continue iterating, increasing the index by 1 on each iteration.
    - Stop iterating once the penultimate char has been moved to the end (so the char at index position length - 1 (off by one error?))
Coerce back to an integer and return

"""

def max_rotation(number):
    digits_list = list(str(number))

    for idx in range(len(digits_list) - 1):
        single_digit = digits_list.pop(idx)
        digits_list.append(single_digit)

    return int(''.join(digits_list))

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# # Note that the final sequence here is `015`. The leading
# # zero gets dropped, though, since we're working with
# # an integer.
print(max_rotation(105) == 15)                 # True