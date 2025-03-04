# 

"""
- sorted_list = lst1[0]
- for el in lst2
- for idx in range((len(sorted_list) - 1))
    - if length of sorted_list is 1:
        - if el is =< element at sorted_list[idx] - add el to start of list
        - else if num is > element at sorted_list[idx] - add el to end of list
    - else:
        - if el is =< element at sorted_list[idx] - add el to sorted_list[idx   -1 ]
        - elif el is > element at sorted_list[idx] and < element at sorted_list[idx + 1] - insert el at sorted_list[idx + 1]
        elif el is > element at sorted_list[idx + 1] - insert el at sorted_list[idx + 2]



"""
# All of these examples should print True

def sort_the_list(sorted_list, el):
    if not sorted_list or el <= sorted_list[0]:
        sorted_list.insert(0, el)
    elif el >= sorted_list[-1]:
        sorted_list.append(el)
    else:
        for idx in range(len(sorted_list) - 1):
            if (el >= sorted_list[idx]) and (el < sorted_list[idx + 1]):
                sorted_list.insert(idx + 1, el)
                break
    
    return sorted_list

def merge(lst1, lst2):
    if not lst2:
        return lst1

    sorted_list = lst1[:]
    for el in lst2:
        sorted_list = sort_the_list(sorted_list, el)
    
    return sorted_list

print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)

