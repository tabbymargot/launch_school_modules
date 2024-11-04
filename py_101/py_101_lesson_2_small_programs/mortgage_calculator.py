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

def is_valid_unit(time_unit_str):
    match time_unit_str:
        case 'm' | 'y' :
            return True
        case _:
            return False
        
def remove_leading_zeros(num_str):
    while num_str != '':
        if (num_str[0] == '0'):
            num_str = num_str[1:]
        elif (num_str[0] != '0'):
            break
        
    if num_str == '':
        return '0'
    else:  
        return num_str
        
def remove_percent_symbol(number_str):

    chars = ['%']

    for char in chars:
        if char in number_str:
            print(f'This is the char: {char}')
            number_str = number_str.replace(char, '')
            print(number_str)

    return number_str




# FUNCTIONS FOR GETTING INPUT
        
def get_loan_amount():
    loan_amount = 0

    while loan_amount < 1:
        prompt('How much would you like to borrow in USD?')
        loan_amount_str = input()

        loan_amount_str = remove_leading_zeros(loan_amount_str)

        if loan_amount_str == '0':
            prompt("The amount must be greater than 0. Please try again.")
        elif '.' in loan_amount_str:
            prompt("The amount cannot contain a decimal point. Please try again.")
        elif loan_amount_str.isdigit() == False:
            prompt("Your amount should contain only digits. Please try again.")
        else:
            loan_amount = int(loan_amount_str)
            return loan_amount     

def get_apr():
    # TODO adjust for US way of entering rates, ie 0.05%
    cleaned_rate = ''

    while cleaned_rate == '':
        prompt("""What is the annual interest rate?
        Please enter the rate either as a whole number
        or as a decimal. For example, if the annual 
        interest rate is 5% you could enter 5 or 5.0
        """)
        annual_rate_str = input()

        try: 
            cleaned_rate = float(remove_percent_symbol(annual_rate_str))
        except ValueError:
            prompt("Unfortunately that is not a valid APR. Please try again")

    apr = cleaned_rate / 1000
    return apr

def get_time_unit():
    while True:
        (prompt("""Would you like to enter the duration of your loan in months or years?
        Enter 'M' for months.
        Enter 'Y' for years\n"""
            ))
        
        time_unit_str = input()[0].lower()
        validation_status = is_valid_unit(time_unit_str)
        
        match validation_status:
            case True:
                return time_unit_str
            case False:
                prompt("Unfortunately that is not a valid duration.")

def get_duration():
    if time_unit_str == 'y':
        while True:
            prompt('Over how many years will you be paying off your loan?')
            duration_in_years_str = input()

            if duration_in_years_str.isdigit() == False:
                prompt("The loan duration should contain only digits. Please try again.")
            else: 
                duration_in_months = int(duration_in_years_str) * 12
                break 
    elif time_unit_str == 'm':
        while True:
            prompt('Over how many months will you be paying off your loan?')
            duration_in_months_str = input()

            if duration_in_months_str.isdigit() == False:
                prompt("The loan duration should contain only digits. Please try again.")
            else:
                duration_in_months = int(duration_in_months_str)
                break
    
    return duration_in_months

loan_amount = get_loan_amount()

apr = get_apr()
# print(apr)

time_unit_str = get_time_unit()
duration_in_months = get_duration()



monthly_interest_rate = apr / 12
print(f'Monthly interest rate: {monthly_interest_rate}')

monthly_payment = loan_amount * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-duration_in_months)))


monthly_payment = loan_amount * (monthly_interest_rate /
(1 - ((1 + monthly_interest_rate)**(-duration_in_months))))
print(f'Your monthly repayment will be: ${monthly_payment:.2f}')