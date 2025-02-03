import os
import pdb
import random

# def prompt(message):
#     print(f'==> {message}')

WHO_GOES_FIRST = 'choose'
INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = '0'
GAMES_TO_WIN_MATCH = 5
WINNING_LINES = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
        [1, 5, 9], [3, 5, 7]              # diagonals
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

def player_chooses_square(board):

    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Choose a square ({join_or(valid_choices)}):")
        square = input().strip()
        if square in valid_choices:
            break
        
        prompt("Sorry, that's not a valid choice.")
    
    board[int(square)] = 'X'

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

def find_at_risk_square(line, board, marker):
    # For each square in line, get the value associated with that square (key) in the board dictionary and assign them to a list markers_in_line:
    # Line looks like this: [4, 5, 6]
    # markers_in_line looks like this: [' ', 'X', ' ']
    markers_in_line = [board[square] for square in line]

    markers_in_line = [board[square] for square in line]

    if markers_in_line.count(marker) == 2:
        for square in line:
            # If the square is available (ie at risk)
            if board[square] == INITIAL_MARKER:
                return square
    return None

def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return

    square = None

    # offense first
    for line in WINNING_LINES:
        square = find_at_risk_square(line, board, COMPUTER_MARKER)
        if square:
            break

    # defense
    if not square:
        for line in WINNING_LINES:
            square = find_at_risk_square(line, board, HUMAN_MARKER)
            if square:
                break
    
    # square 5
    if not square:
        for line in WINNING_LINES:
            if 5 in empty_squares(board):
                square = 5
                if square:
                    break

    # just pick a random square
    if not square:
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

def decide_who_goes_first():
    if WHO_GOES_FIRST == 'choose':
        while True:
            prompt("Please choose who plays first. Type 'p' for player or 'c' for 'computer': ")
            first_player = input().strip().lower()

            if first_player == 'p':
                first_player = 'player'
                return first_player
            elif first_player == 'c':
                first_player = 'computer'
                return first_player  

            prompt("Sorry, that's not a valid choice.")

    else:
        first_player = WHO_GOES_FIRST
        return first_player

def play_tic_tac_toe():
    first_player = decide_who_goes_first()
    player_score = 0
    computer_score = 0
    while True:
        board = initialize_board()

        while True:

            if first_player == 'computer':

                    computer_chooses_square(board)
                    display_board(board)   
                    if someone_won(board) or board_full(board):
                        break
                    
                    # print('Computer chose...')

                    player_chooses_square(board)
                    if someone_won(board) or board_full(board):
                        break
          
            elif first_player == 'player':
                display_board(board)

                player_chooses_square(board)
                if someone_won(board) or board_full(board):
                    break

                computer_chooses_square(board)
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