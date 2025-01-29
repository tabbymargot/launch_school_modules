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
        if char.isalpha():
            if (not new_string) or letters[-1].islower():
                letters, new_string = add_uppercase_letter(letters, new_string, char)
            else:
                letters, new_string = add_lowercase_letter(letters, new_string, char)
        else:
            new_string += char

    return new_string


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