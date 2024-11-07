import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'spock', 'scissors']

def prompt(message):
    print(f"==> {message}")

def get_choice(word_choice):
    while word_choice is None:
        prompt("That's not a valid choice")
        player_choice = input()
        word_choice = abbreviations.get(player_choice)

    return word_choice

def compute_game_winner():
    if (((full_word_choice == "rock" and
         computer_choice == ("scissors" or "lizard"))) or
        ((full_word_choice == "scissors" and
        computer_choice == ("paper" or "lizard"))) or
        ((full_word_choice == "paper" and
        computer_choice == ("rock" or "spock"))) or
        ((full_word_choice == "spock" and
        computer_choice == ("scissors" or "rock"))) or
        ((full_word_choice == "lizard" and
        computer_choice == ("paper" or "spock")))):
        return 'player_wins'

    if (((full_word_choice == "rock" and
        computer_choice == ("paper" or "spock"))) or
        ((full_word_choice == "paper" and
        computer_choice == ("scissors" or "lizard"))) or
        ((full_word_choice == "scissors" and
        computer_choice == ("rock" or "spock"))) or
        ((full_word_choice == "spock" and
        computer_choice == ("lizard" or "paper"))) or
        ((full_word_choice == "scissors" and
        computer_choice == ("rock" or "spock")))):
        return 'computer_wins'

    return 'tie'

def display_game_winner(the_result):
    if the_result == 'player_wins':
        prompt('You win!\n')
    elif the_result == 'computer_wins':
        prompt('Computer wins!\n')
    else:
        prompt("It's a tie.\n")

def increment_score(the_result, player_score, computer_score):
    if the_result == 'player_wins':
        player_score += 1
    elif the_result == 'computer_wins':
        computer_score += 1

    return player_score, computer_score

def display_scores(player_score, computer_score):
    prompt(f"Your score is {player_score}.")
    prompt(f"The computer's score is {computer_score}.\n")

def display_grand_winner(player_score, computer_score):
    if player_score == 3:
        prompt('You are the grand winner!')
    elif computer_score == 3:
        prompt('The computer is the grand winner!')
    else:
        pass

def get_continuation_preference():
    while player_current_score == 3 or computer_current_score == 3:
        prompt("Do you want to play again (y/n)?")
        answer = input().lower()

        if answer.startswith('n') or answer.startswith('y'):
            return answer
        else:
            prompt("That's not a valid choice")

player_current_score = 0
computer_current_score = 0
continuation_preference = ''

prompt('Welcome to Best of Five!')

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

    validated_player_choice = get_choice(full_word_choice)

    computer_choice = random.choice(VALID_CHOICES)

    prompt(f"You chose {validated_player_choice}, computer chose {computer_choice}")

    result = compute_game_winner()

    display_game_winner(result)

    player_current_score, computer_current_score =  (increment_score
                                                    (result,
                                                    player_current_score,
                                                    computer_current_score))

    display_scores(player_current_score, computer_current_score)

    display_grand_winner(player_current_score, computer_current_score)

    continuation_preference = get_continuation_preference()

    match continuation_preference:
        case None:
            pass # Best of Five game not yet finished; continue looping.
        case 'n':
            break
        case 'y':
            player_current_score = 0
            computer_current_score = 0
            continuation_preference = ''