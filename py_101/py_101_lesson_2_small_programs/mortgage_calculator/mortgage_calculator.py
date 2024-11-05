# HELPER FUNCTIONS
def prompt(message):
    print(f'==> {message}')

# TODO move prompts to JSON file.

while True:
        
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
                prompt("The interest rate must be greater than 0. Please try again.")
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
                    prompt("Unfortunately your entry does not represent a valid unit of time. Please try again.")

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
                continue

            if duration_in_months <= 0:
                prompt("The duration of your loan must be at least 1 month. Please try again.")
            else: 
                return duration_in_months
    
    def get_continuation_preference():
        while True:
            (prompt(f"""Would you like to perform another calculation? 
            Enter 'Y' for 'yes' 
            Enter 'N' for 'no'."""
            ))
            
            answer = input()[0].lower()

            match answer:
                case 'y':
                    return 'y'
                case 'n':
                    return 'n'
                case _:
                    prompt("Unfortunately your entry isn't valid. Please try again.")
    
    # REQUEST AND VALIDATE INPUT

    loan_amount = get_loan_amount()

    apr = get_apr()

    time_unit_str = get_time_unit()

    match time_unit_str:
        case 'y':
            duration_in_months = get_duration_in_years() * 12
        case 'm':
            duration_in_months = get_duration_in_months()

    # CALCULATE AND OUTPUT MONTHLY REPAYMENT

    monthly_interest_rate = apr / 12

    monthly_payment = loan_amount * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-duration_in_months)))

    prompt(f'Your monthly repayment will be: ${monthly_payment:.2f}')
    answer = get_continuation_preference()
    
    if answer == 'n':
        break