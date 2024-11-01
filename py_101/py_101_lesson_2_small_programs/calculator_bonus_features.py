import json

# Load the messages from the JSON file
with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

while True:
    def prompt(message):
        print(f"==> {message}")

    def invalid_number(number_str):
        try:
            float(number_str)
        except ValueError:
            return True

        return False

    prompt(MESSAGES['Welcome'])

    prompt(MESSAGES['First'])
    number1 = input()

    while invalid_number(number1):
        prompt(MESSAGES['Not_valid'])
        number1 = input()

    prompt(MESSAGES['Second'])
    number2 = input()

    while invalid_number(number2):
        prompt(MESSAGES['Not_valid'])
        number2 = input()

    prompt(MESSAGES['Operation'])
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(MESSAGES['Choose'])
        operation = input()

    match operation:
        case "1":
            output = float(number1) + float(number2)
        case "2":
            output = float(number1) - float(number2)
        case "3":
            output = float(number1) * float(number2)
        case "4":
            output = float(number1) / float(number2)

    prompt(f'The result is {output:.2f}')

    prompt(MESSAGES['Continue?'])
    carry_on = input()

    if carry_on == 'N':
        print("Goodbye!")
        break