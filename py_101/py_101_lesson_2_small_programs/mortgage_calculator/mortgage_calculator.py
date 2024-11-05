import json

with open('mortgage_calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

# HELPER FUNCTIONS
def prompt(message):
    print(f'==> {message}')

while True:

    def get_loan_amount():

        while True:
            prompt(MESSAGES['request_loan_amount'])
            loan_amount_str = input()

            try:
                int(loan_amount_str)
            except ValueError:
                prompt(MESSAGES['invalid_loan_amount'])
                continue
            else:
                loan_amount = int(loan_amount_str)

            if loan_amount <= 0:
                prompt(MESSAGES['amount_too_low'])
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
                continue
            else:
                annual_rate_float = float(annual_rate_str)

            if annual_rate_float <= 0:
                prompt(MESSAGES['rate_too_low'])
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

    def get_duration_in_years():
        while True:
            prompt(MESSAGES['request_loan_duration_in_years'])
            duration_in_years_str = input()

            try:
                int(duration_in_years_str)
            except ValueError:
                prompt(MESSAGES['invalid_loan_duration'])
                continue
            else:
                duration_in_years = int(duration_in_years_str)

            if duration_in_years <= 0:
                prompt(MESSAGES['too_few_years'])
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
                continue
            else:
                duration_in_months = int(duration_in_months_str)

            if duration_in_months <= 0:
                prompt(MESSAGES['too_few_months'])
            else:
                return duration_in_months

    def get_continuation_preference():
        while True:
            prompt(MESSAGES['continue?'])

            answer = input()[0].lower()

            match answer:
                case 'y':
                    return 'y'
                case 'n':
                    return 'n'
                case _:
                    prompt(MESSAGES['invalid_entry'])

    # REQUEST AND VALIDATE INPUT

    final_loan_amount = get_loan_amount()

    final_apr = get_apr()

    final_time_unit_str = get_time_unit()

    match final_time_unit_str:
        case 'y':
            final_duration_in_months = get_duration_in_years() * 12
        case 'm':
            final_duration_in_months = get_duration_in_months()

    # CALCULATE AND OUTPUT MONTHLY REPAYMENT

    monthly_interest_rate = final_apr / 12

    monthly_payment = (final_loan_amount *
                    (monthly_interest_rate /
                    (1 - (1 + monthly_interest_rate) **
                    (-final_duration_in_months))))

    prompt(f'Your monthly repayment will be: ${monthly_payment:.2f}')

    # CONFIRM IF USER WISHES TO CONTINUE

    continuation_preference = get_continuation_preference()

    if continuation_preference == 'n':
        break