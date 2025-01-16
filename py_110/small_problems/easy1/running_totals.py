def running_total(lst):
    if not lst:
        return lst
    
    running_totals = []

    for num in lst:
        if not running_totals:
            running_totals.append(num)
        else:
            running_totals.append(num + running_totals[-1])

    return running_totals


print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20]) == [14, 25, 32, 47, 67]) #True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True