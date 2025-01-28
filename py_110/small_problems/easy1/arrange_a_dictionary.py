def k_v_pair_key(key_value_pair):
    the_key, the_value = key_value_pair
    return the_value

def order_by_value(my_dict):
    list_of_keys = []
    list_of_values = []
    for key, value in my_dict.items():
        list_of_keys.append(key)
        list_of_values.append(value)

    sorted_keys_and_values = sorted(zip(list_of_keys, list_of_values), key=k_v_pair_key)

    return [key_value_pair[0] 
            for key_value_pair in sorted_keys_and_values]

my_dict = {'p': 8, 'q': 2, 'r': 6}
list_of_keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == list_of_keys)  # True