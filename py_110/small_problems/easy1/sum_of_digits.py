def sum_digits(num):
    running_total = 0
    for num_str in list(str(num)):
        running_total += int(num_str)
    return running_total


print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True