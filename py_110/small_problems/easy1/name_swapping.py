def swap_name(whole_name):
    first_name, last_name = whole_name.split(' ')
    return f'{last_name}, {first_name}'


print(swap_name('Joe Roberts') == "Roberts, Joe")   # True