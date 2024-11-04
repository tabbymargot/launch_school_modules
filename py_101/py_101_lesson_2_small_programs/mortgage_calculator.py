"""
Get the loan amount
Get the APR
Get the duration

Calculate the monthly interest rate (APR / 12)
Calculate the loan duration in months

"""

def prompt(message):
    print(f'==> {message}')

# VALIDATION FUNCTIONS
        
# def remove_leading_zeros(num_str):
#     while num_str != '':
#         if (num_str[0] == '0'):
#             num_str = num_str[1:]
#         elif (num_str[0] != '0'):
#             break
        
#     if num_str == '':
#         return '0'
#     else:  
#         return num_str
    
# FUNCTIONS TO BE ORGANISED

def get_duration_in_years():
    while True:
        prompt('Over how many years will you be paying off your loan?')
        duration_in_years_str = input()

        try: 
            duration_in_years = int(duration_in_years_str)
        except ValueError:
            prompt("The loan duration should contain only digits. Please try again.")
            continue

        if duration_in_years <= 0:
            prompt("The duration of your loan must be at least 1 year. Please try again.")
        else: 
            return duration_in_years
        
def get_duration_in_months():
    while True:
        prompt('Over how many months will you be paying off your loan?')
        duration_in_months_str = input()

        try: 
            duration_in_months = int(duration_in_months_str)
        except ValueError:
            prompt("The loan duration should contain only digits. Please try again.")

        if duration_in_months <= 0:
            prompt("The duration of your loan must be at least 1 month. Please try again.")
        else: 
            return duration_in_months



# FUNCTIONS FOR GETTING INPUT

# TODO move prompts to JSON file.
        
def get_loan_amount():

    while True:
        prompt('How much would you like to borrow in USD?')
        loan_amount_str = input()

        try: loan_amount = int(loan_amount_str)
        except ValueError:
            prompt("Your amount should contain only digits. Please try again.")
            continue

        if loan_amount <= 0:
            prompt("Your amount must be greater than 0. Please try again.")
        else: 
            break

    return loan_amount 

def get_apr():

    while True:
        prompt("""What is the annual interest rate?
    Please enter the rate either as a whole number
    or as a decimal. For example, if the annual 
    interest rate is 5% you could enter 5 or 5.0
        
    Note that the annual interest rate must be greater 
    than 0.
    """)
        annual_rate_str = input()

        if annual_rate_str.endswith('%'):
            annual_rate_str = annual_rate_str[:-1]

        try: 
            annual_rate_float = float(annual_rate_str)
        except ValueError:
            prompt("Unfortunately that is not a valid APR. Please try again")
            continue
        
        if annual_rate_float <= 0:
            prompt("Your amount must be greater than 0. Please try again.")
        else: 
            break

    apr = annual_rate_float / 100
    return apr

def get_time_unit():
    while True:
        (prompt("""Would you like to enter the duration of your loan in months or years?
        Enter 'M' for months.
        Enter 'Y' for years\n"""
            ))
        
        time_unit_str = input()[0].lower()

        match time_unit_str:
            case 'm' | 'y' :
                return time_unit_str
            case _:
                prompt("Unfortunately that is not a valid unit of time. Please try again.")

def get_duration():
    if time_unit_str == 'y':
        duration_in_months = get_duration_in_years() / 12
    elif time_unit_str == 'm':
        duration_in_months = get_duration_in_months()
    
    return duration_in_months

loan_amount = get_loan_amount()
print(f'loan_amount: {loan_amount}')

apr = get_apr()
print(f'APR: {apr}')

time_unit_str = get_time_unit()
print(f'time_unit_str: {time_unit_str}')
duration_in_months = get_duration()
print(f'duration_in_months: {duration_in_months}')



monthly_interest_rate = apr / 12
print(f'Monthly interest rate: {monthly_interest_rate}')

monthly_payment = loan_amount * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-duration_in_months)))

print(f'Your monthly repayment will be: ${monthly_payment:.2f}')