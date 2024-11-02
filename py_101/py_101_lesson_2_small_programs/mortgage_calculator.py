"""
Get the loan amount
Get the APR
Get the duration

Calculate the monthly interest rate (APR / 12)
Calculate the loan duration in months

"""

def prompt(message):
    print(f'==> {message}')

def is_valid_unit(time_unit):
    match time_unit:
        case 'm' | 'y' | 'months' | 'years' :
            return True
        case _:
            return False
        
def get_time_unit():
    while True:
        (prompt("""Would you like to enter the duration of your loan in months or years?
        Enter 'M' for months.
        Enter 'Y' for years\n"""
            ))
        
        time_unit = input().lower()
        validation_status = is_valid_unit(time_unit)
        
        match validation_status:
            case True:
                return time_unit
            case False:
                prompt("Unfortunately that is not a valid duration.")

def validate_rate(rate_str):
    # TODO Is validate a good name if we're actually making changes?
    if rate_str.endswith('%'):
        rate_str = rate_str[:-1]
    
    return rate_str



# def calculate_monthly_interest_rate(apr):
#     return apr / 12

# prompt('How much would you like to borrow?')
# loan_amount = float(input())
# print(f'Loan amount: {loan_amount}')

# TODO make this a function similar to get_time_unit()
prompt("""What is the annual interest rate?
    Please enter the rate either as a whole number
    or as a decimal. For example, if the annual 
    interest rate is 5% you could enter 5 or 5.0
""")
annual_rate_str = input()

# TODO try / except for invalid inputs?
validated_rate = validate_rate(annual_rate_str)
print(validated_rate)

# apr = annual_rate_str / 100
# print(f'APR: {apr}')

# time_unit = get_time_unit()

# prompt('Over how many years will you be paying off your loan?')
# duration_in_years = int(input())
# print(f'Duration in years: {duration_in_years}')

# duration_in_months = duration_in_years * 12
# print(f'Duration in months: {duration_in_months}')

# monthly_interest_rate = apr / 12
# print(f'Monthly interest rate: {monthly_interest_rate}')

# monthly_payment = loan_amount * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-duration_in_months)))


# monthly_payment = loan_amount * (monthly_interest_rate /
# (1 - ((1 + monthly_interest_rate)**(-duration_in_months))))
# print(f'Monthly payment: {monthly_payment}')