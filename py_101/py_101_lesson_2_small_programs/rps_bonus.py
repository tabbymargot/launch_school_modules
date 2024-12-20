import random

VALID_CHOICES_LEGEND = {
        'r': 'rock',
        'p': 'paper',
        'sc': 'scissors',
        'sp': 'spock',
        'l': 'lizard',
    }

VALID_CHOICES = list(VALID_CHOICES_LEGEND.values())

WINNING_COMBOS = {
    'rock':     ['scissors', 'lizard'],
    'paper':    ['rock',     'spock'],
    'scissors': ['paper',    'lizard'],
    'lizard':   ['paper',    'spock'],
    'spock':    ['rock',     'scissors'],
}

PLAYER_WINS = 'player_wins'
COMPUTER_WINS = 'computer_wins'
TIE = 'tie'

player_current_score = 0
computer_current_score = 0
continuation_preference = ''

def prompt(message):
    print(f"==> {message}")

def get_choice(word_choice):
    while word_choice is None:
        prompt("That's not a valid choice")
        the_player_choice = input().lower()
        word_choice = VALID_CHOICES_LEGEND.get(the_player_choice)

    return word_choice

def compute_game_winner(the_player_choice, the_computer_choice):
    if the_computer_choice in WINNING_COMBOS[the_player_choice]:
        return COMPUTER_WINS

    if the_player_choice in WINNING_COMBOS[the_computer_choice]:
        return PLAYER_WINS

    return TIE

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

def display_grand_winner(player_current_score, computer_current_score):
    if player_current_score == 3:
        prompt('You are the grand winner!')
    elif computer_current_score == 3:
        prompt('The computer is the grand winner!')

def get_continuation_preference():
    while True:
        prompt("Do you want to play again (y/n)?")
        answer = input().lower()

        if (answer.startswith('n') is False) and\
        (answer.startswith('y') is False):
            prompt("That's not a valid choice")
        else:
            return answer[0]

prompt('Welcome to Best of Five!\n')

while True:
    prompt('Choose one of the following:')

    for first_letter, full_word in VALID_CHOICES_LEGEND.items():
        prompt(f"Type '{first_letter}' for '{full_word}'")

    choice = input().lower()

    player_choice = VALID_CHOICES_LEGEND.get(choice)

    validated_player_choice = get_choice(player_choice)

    computer_choice = random.choice(VALID_CHOICES)

    prompt(f"You chose {validated_player_choice}, "
            f"computer chose {computer_choice}")

    result = compute_game_winner(validated_player_choice, computer_choice)

    display_game_winner(result)

    player_current_score, computer_current_score =  (increment_score
                                                    (result,
                                                    player_current_score,
                                                    computer_current_score))

    display_scores(player_current_score, computer_current_score)

    if player_current_score == 3 or computer_current_score == 3:
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