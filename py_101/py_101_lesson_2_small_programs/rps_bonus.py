import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'spock', 'scissors']

def prompt(message):
    print(f"==> {message}")

# def calculate_overall_winner(player_score, computer_score):
#     while player_score < 3 or computer_score < 3:
#         player_score += player_score
#         computer_score += computer_score

#     if player_score == 3:
#         return player_score
#     else:
#         return computer_score 

def display_winner():
    if ((full_word_choice == "rock" and computer_choice == ("scissors" or "lizard")) or
        (full_word_choice == "scissors" and computer_choice == ("paper" or "lizard")) or
        (full_word_choice == "paper" and computer_choice == ("rock" or "spock")) or
        (full_word_choice == "spock" and computer_choice == ("scissors" or "rock")) or
        (full_word_choice == "lizard" and computer_choice == ("paper" or "spock"))):
        prompt("You win!")
    elif ((full_word_choice == "rock" and computer_choice == ("paper" or "spock")) or
        (full_word_choice == "paper" and computer_choice == ("scissors" or "lizard")) or
        (full_word_choice == "scissors" and computer_choice == ("rock" or "spock")) or
        (full_word_choice == "spock" and computer_choice == ("lizard" or "paper")) or
        (full_word_choice == "scissors" and computer_choice == ("rock" or "spock"))):
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")

# def calculate_winner():

player_score = 0
computer_score = 0
answer = ''

prompt(f'Welcome to Best of Five!')

while True:

    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input()

    abbreviations = {
        'r': 'rock',
        'p': 'paper',
        'sc': 'scissors',
        'sp': 'spock',
        'l': 'lizard',
    }

    full_word_choice = abbreviations.get(choice)

    while full_word_choice == None:
        prompt("That's not a valid choice")
        choice = input()
        full_word_choice = abbreviations.get(choice)

    computer_choice = random.choice(VALID_CHOICES)

    prompt(f"You chose {full_word_choice}, computer chose {computer_choice}")

    display_winner()

    if ((full_word_choice == "rock" and computer_choice == ("scissors" or "lizard")) or
        (full_word_choice == "scissors" and computer_choice == ("paper" or "lizard")) or
        (full_word_choice == "paper" and computer_choice == ("rock" or "spock")) or
        (full_word_choice == "spock" and computer_choice == ("scissors" or "rock")) or
        (full_word_choice == "lizard" and computer_choice == ("paper" or "spock"))):

        player_score += 1
        print(f'player score: {player_score}')

    elif ((full_word_choice == "rock" and computer_choice == ("paper" or "spock")) or
        (full_word_choice == "paper" and computer_choice == ("scissors" or "lizard")) or
        (full_word_choice == "scissors" and computer_choice == ("rock" or "spock")) or
        (full_word_choice == "spock" and computer_choice == ("lizard" or "paper")) or
        (full_word_choice == "scissors" and computer_choice == ("rock" or "spock"))):

        computer_score += 1
        print(f'computer score: {computer_score}')

    if player_score == 3:
        prompt('You are the overall winner!')
    elif computer_score == 3:
        prompt('The computer is the overall winner!')
    else:
        pass

    while player_score == 3 or computer_score == 3:
        prompt("Do you want to play again (y/n)?")
        answer = input().lower()

        if answer.startswith('n') or answer.startswith('y'):
            break
        else:
            prompt("That's not a valid choice")

    if answer == '':
        pass
    elif answer[0] == 'n':
        break
    elif answer[0] == 'y':
        player_score = 0
        computer_score = 0
        answer = ''