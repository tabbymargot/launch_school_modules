import json

with open('mortgage_calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

from time import sleep

def display_welcome_message():
    prompt('Welcome to The Loan Calculator! \U0001F44B\n')
    sleep(1.5)

def prompt(message):
    print(f'==> {message}')

def implement_pause():
    sleep(1.5)

def display_divider():
    sleep(0.5)
    print('\n'
        '********************************'
        '\n')

def display_emojis():
    counter = 3
    while counter > 0:
        sleep(1)
        print('\U0001F630\n')

        counter -= 1

    sleep(1)

display_welcome_message()

while True:
    def get_loan_amount():
        while True:
            prompt(MESSAGES['request_loan_amount'])
            loan_amount_str = input()

            try:
                int(loan_amount_str)
            except ValueError:
                prompt(MESSAGES['invalid_loan_amount'])
                implement_pause()
                continue
            else:
                loan_amount = int(loan_amount_str)

            if loan_amount <= 0:
                prompt(MESSAGES['amount_too_low'])
                implement_pause()
            else:
                break

        return loan_amount

    def get_apr():
        while True:
            prompt(MESSAGES['request_annual_rate'])
            annual_rate_str = input()

            if annual_rate_str.endswith('%'):
                annual_rate_str = annual_rate_str[:-1]

            try:
                float(annual_rate_str)
            except ValueError:
                prompt(MESSAGES['apr_not_valid'])
                implement_pause()
                continue
            else:
                annual_rate_float = float(annual_rate_str)

            if annual_rate_float <= 0:
                prompt(MESSAGES['rate_too_low'])
                implement_pause()
            else:
                break

        apr = annual_rate_float / 100
        return apr

    def get_time_unit():
        while True:
            prompt(MESSAGES['request_time_unit'])

            time_unit_str = input()[0].lower()

            match time_unit_str:
                case 'm' | 'y' :
                    return time_unit_str
                case _:
                    prompt(MESSAGES['invalid_time_unit'])
                    implement_pause()

    def get_duration_in_years():
        while True:
            prompt(MESSAGES['request_loan_duration_in_years'])
            duration_in_years_str = input()

            try:
                int(duration_in_years_str)
            except ValueError:
                prompt(MESSAGES['invalid_loan_duration'])
                implement_pause()
                continue
            else:
                duration_in_years = int(duration_in_years_str)

            if duration_in_years <= 0:
                prompt(MESSAGES['too_few_years'])
                implement_pause()
            else:
                return duration_in_years

    def get_duration_in_months():
        while True:
            prompt(MESSAGES['request_loan_duration_in_months'])
            duration_in_months_str = input()

            try:
                int(duration_in_months_str)
            except ValueError:
                prompt(MESSAGES['invalid_loan_duration'])
                implement_pause()
                continue
            else:
                duration_in_months = int(duration_in_months_str)

            if duration_in_months <= 0:
                prompt(MESSAGES['too_few_months'])
                implement_pause()
            else:
                return duration_in_months

    def get_continuation_preference():
        while True:
            prompt(MESSAGES['continue?'])
            implement_pause()

            answer = input()[0].lower()

            match answer:
                case 'y':
                    return 'y'
                case 'n':
                    return 'n'
                case _:
                    prompt(MESSAGES['invalid_entry'])

    def display_monthly_payment():
        print('Your monthly repayment will be...\n')

        display_emojis()

        print(f'${monthly_payment:.2f} \U0001F631\n')

        sleep(2)

    validated_loan_amount = get_loan_amount()
    display_divider()

    validated_apr = get_apr()
    display_divider()

    validated_time_unit_str = get_time_unit()
    display_divider()

    match validated_time_unit_str:
        case 'y':
            validated_duration_in_months = get_duration_in_years() * 12
        case 'm':
            validated_duration_in_months = get_duration_in_months()
    display_divider()

    monthly_interest_rate = validated_apr / 12

    monthly_payment = (validated_loan_amount *
                    (monthly_interest_rate /
                    (1 - (1 + monthly_interest_rate) **
                    (-validated_duration_in_months))))

    display_monthly_payment()
    display_divider()

    continuation_preference = get_continuation_preference()

    if continuation_preference == 'n':
        print('\nNo problem! Hope to see you again soon!')
        break