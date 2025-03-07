""" 

PROBLEM
Restate in my words
Inputs - list
Outputs - lst

EXPLICIT / IMPLICIT REQUIREMENTS
- elements can be integers or strings
- mutate the list during iteration
Clarifying questions
Edge cases

DATA STRUCTURES
ALGORITHM
High level - Iterate through the list, getting 2 elements at a time. If the left element is greater than the right element, swap them. 
Alternative High Level?
Actual algorithm
- Outer loop
    - Inner loop
        - Set flag swaps_made to False to keep track of whether any swaps were made
        - Iterate through the list, getting 2 elements at a time. 
        - Will need to stop before last element is reached:
            - if idx == length of list minus 2
            - break out of inner loop
        - Compare the 2 elements. 
            - If the first is greater than the second:
                swap them
                - If flag == False:    
                    - toggle flag to True
            - Else:
                continue to the next pair
    - If swaps_made == True
        -Restart outer loop

return list


"""

def swap_elements(lst, swaps_made):
    for idx in range(len(lst) - 1):
            first_element = lst[idx]
            second_element = lst[idx + 1]

            if first_element > second_element:
                popped_element = lst.pop(idx)
                lst.insert(idx + 1, popped_element)

                if swaps_made == False:
                    swaps_made = True

    return lst, swaps_made

def bubble_sort(lst):
    while True:
        swaps_made = False

        lst, swaps_made = swap_elements(lst, swaps_made)
        
        if swaps_made == False:
            break # break out of while loop

    return lst

# def bubble_sort(lst):
#     swapped = True # set the flag to True
#     while swapped:
#         swapped = False # immediately set it to False
#         for i in range(len(lst) - 1):
#             if lst[i] > lst[i + 1]:
#                 lst[i], lst[i + 1] = lst[i + 1], lst[i]
#                 swapped = True # if a swap happened, set it back to True. 
#                 # If a swap didn't happen:
#                 # - it means the list is now sorted
#                 # - swapped stays set to False
#                 # - the while loop stops iterating.
#     return lst


lst1 = [7, 5, 3, 4]
bubble_sort(lst1)
print(lst1 == [3, 4, 5, 7])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True