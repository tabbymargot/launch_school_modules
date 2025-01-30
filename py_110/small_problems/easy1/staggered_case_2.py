# MY SOLUTION

def add_uppercase_letter(letters, new_string, char):
    letters += char.upper()
    new_string += char.upper()

    return letters, new_string

def add_lowercase_letter(letters, new_string, char):
    letters += char.lower()
    new_string += char.lower()

    return letters, new_string

def staggered_case(string):
    letters = ""
    new_string = ""

    for char in string:
        # 1. Check the char. 
        # If char is a letter, take action on both the new_string and the tracking string. I'm doing too many things at once. There are notes about this in Capacities.
        if char.isalpha():
            if (not new_string) or letters[-1].islower():
                letters, new_string = add_uppercase_letter(letters, new_string, char)
            else:
                letters, new_string = add_lowercase_letter(letters, new_string, char)
        else:
            new_string += char

    return new_string

# SOLUTION FROM SUBMITTED SOLUTIONS ON EXERCISE PAGE - SIMILAR BUT MUCH CLEANER

# def staggered_case(string):
#     output = []
#     last_alpha = ''

#     for char in string:
#         # 1. Check the tracked letter. Then take action on the output string.
#         # If the tracked letter is lower or the string is empty:
#         if last_alpha.islower() or not last_alpha:
#             # Set the char to upper
#             char = char.upper()
#         else:
#             # Else set the char to lower
#             char = char.lower()
#         #Append char to output
#         output.append(char)

#         # 2. Check the char. Then take action on the tracking string.
#         # If it's a letter, append it to last_alpha. 
#         # By this stage it's already been set to upper or lower.
#         if char.isalpha():
#             last_alpha = char

#     return ''.join(output)


string = 'I L'
string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

# string = "ignore 77"
string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True