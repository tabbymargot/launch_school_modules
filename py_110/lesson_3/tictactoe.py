import random

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = '0'

def display_board(board):
    # pass
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
        prompt(f"Choose a square ({', '.join(valid_choices)}):")
        square = input().strip()
        if square in valid_choices:
            break
        
        prompt("Sorry, that's not a valid choice.")
    
    board[int(square)] = 'X'

def computer_chooses_square(board):
    square = random.choice(empty_squares(board))
    board[square] = COMPUTER_MARKER

def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

board = initialize_board()
display_board(board)

player_chooses_square(board)
display_board(board)