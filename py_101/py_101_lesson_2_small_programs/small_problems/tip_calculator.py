""" 
Prompt for the bill amount
Prompt for the tip percentage.
Calculate the tip
Calculate the total bill
Print the tip and the total bill
"""

bill = float(input('What is the bill? '))
tip_percentage = float(input('What is the tip percentage? '))

tip_amount = (bill / 100) * tip_percentage

print(f'The tip is ${tip_amount:.2f}')
print(f'The total is ${tip_amount + bill:.2f}')
