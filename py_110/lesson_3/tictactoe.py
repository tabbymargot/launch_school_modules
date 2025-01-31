import os
import pdb
import random

COMPUTER_MARKER = '0'
GAMES_TO_WIN_MATCH = 5
HUMAN_MARKER = 'X'
INITIAL_MARKER = ' '
# Changed sublists to sets to use in get_threat
WINNING_LINES = [
    {1, 2, 3}, {4, 5, 6}, {7, 8, 9},  # rows
    {1, 4, 7}, {2, 5, 8}, {3, 6, 9},  # columns
    {1, 5, 9}, {3, 5, 7}              # diagonals
]

def display_board(board):
    # os.system('clear')

    prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.")
    print('')
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print('     |     |')
    print('')

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def prompt(message):
    print(f'==> {message}')

def get_threat(player_choices, board):
    valid_choices = get_valid_choices(board)

    available_square = None
    if len(player_choices) > 1:
        for line in WINNING_LINES:
            chosen_squares = set()

            for square in line:
                if square in player_choices:
                    chosen_squares.add(square)
        
            if len(chosen_squares) == 2:
                available_square = list(line - chosen_squares)[0]

            # TODO: Create function is_valid?
            if available_square in valid_choices:
                return available_square
    
    return available_square
        
def player_chooses_square(board, player_choices):
    while True:
        valid_choices = get_valid_choices(board)
        prompt(f"Choose a square ({join_or(valid_choices)}):")

        square = int(input().strip())

        if square in valid_choices:
            player_choices.add(square)
            break
        
        prompt("Sorry, that's not a valid choice.")
    
    board[int(square)] = 'X'

    return player_choices

# Created this function as valid choices needed in more than one function
def get_valid_choices(board):
    return [num for num in empty_squares(board)]

def join_or(empty_squares_lst, punctuation=", ", word="or"):
    match len(empty_squares_lst):
        case 0:
            return ""
        case 1:
            return str(empty_squares_lst[0])
        case 2:
            return f'{empty_squares_lst[0]} {word} {empty_squares_lst[1]}'
        
    return ''.join(add_punctuation_and_word(empty_squares_lst, punctuation, word))
        
def add_punctuation_and_word(empty_squares_lst, punctuation, word):
    formatted_list = []

    for num in empty_squares_lst:
        if num != empty_squares_lst[-1]:
            formatted_list.extend([str(num), punctuation])
        else:
            formatted_list.extend([word, ' ', str(num)])
    
    return formatted_list

def computer_chooses_square(board, player_choices):
    if len(empty_squares(board)) == 0:
        return

    threatening_square = get_threat(player_choices, board)
    
    if threatening_square:
        square = threatening_square
    else:
        square = random.choice(empty_squares(board))
    
    board[square] = COMPUTER_MARKER

def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return bool(detect_winner(board))

def detect_winner(board):
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER
                and board[sq2] == HUMAN_MARKER
                and board[sq3] == HUMAN_MARKER):
            return 'Player'
        elif (board[sq1] == COMPUTER_MARKER
                  and board[sq2] == COMPUTER_MARKER
                  and board[sq3] == COMPUTER_MARKER):
            return 'Computer'
        
    return None

def play_tic_tac_toe():
    player_score = 0
    computer_score = 0
    
    while True:
        board = initialize_board()
        player_choices = set()

        while True:
            display_board(board)
            player_choices = player_chooses_square(board, player_choices)

            if someone_won(board) or board_full(board):
                break

            computer_chooses_square(board, player_choices)

            if someone_won(board) or board_full(board):
                break
            

        display_board(board)

        if someone_won(board):
            winner = detect_winner(board)
            if winner == 'Player':
                player_score += 1
            else:
                computer_score += 1
            print(f'Player score: {player_score}')
            print(f'Computer score: {computer_score}')
            prompt(f"{winner} won!")
        else:
            prompt("It's a tie!")
        
        if player_score == GAMES_TO_WIN_MATCH or computer_score == GAMES_TO_WIN_MATCH:
            prompt(f'{winner} wins the match!')
            player_score = 0
            computer_score = 0

        prompt("Play again? (y or n)")
        answer = input().lower()

        if answer[0] != 'y':
            break
    
    prompt('Thanks for playing Tic Tac Toe!')

play_tic_tac_toe()