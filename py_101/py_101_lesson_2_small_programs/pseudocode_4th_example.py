# SNIPPET FOR FINDING NTH INSTANCE OF CHARACTER IN A STRING

def find_third(char, my_string):
    instance_of_char = 0
    index = 0

    if my_string.count(char) < 3:
        return None
    
    for character in my_string:
        if character != char:
            index += 1
        elif character == char and instance_of_char < 3:
            instance_of_char += 1 

            if instance_of_char == 3:
                return index
            else:
                index += 1

char = 'x'
my_string = 'axbxcdxex'
print(find_third(char, my_string))