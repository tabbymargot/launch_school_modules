import random
import os

def clear_screen():
    os.system('clear')

class Square:
    INITIAL_MARKER = " "
    HUMAN_MARKER = "X"
    COMPUTER_MARKER = "O"

    def __init__(self, marker=INITIAL_MARKER):
        self.marker = marker

    def __str__(self):
        # Printing the square will now print its marker instead of
        # the entire object. This is more helpful.
        return self.marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, value):
        self._marker = value

    def is_unused(self):
        return self.marker == Square.INITIAL_MARKER

class Board:
    def __init__(self):
        self.reset()

    def reset(self):
        self.squares = {key: Square() for key in range(1, 10)}

    def display(self):
        print()
        print("     |     |")
        print(f"  {self.squares[1]}  |"
            f"  {self.squares[2]}  |"
            f"  {self.squares[3]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[4]}  |"
            f"  {self.squares[5]}  |"
            f"  {self.squares[6]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[7]}  |"
            f"  {self.squares[8]}  |"
            f"  {self.squares[9]}")
        print("     |     |")
        print()

    def mark_square_at(self, key, marker):
        self.squares[key].marker = marker

    def unused_squares(self):
        return [key
                for key, square in self.squares.items()
                if square.is_unused()]

    def is_full(self):
        return len(self.unused_squares()) == 0

    def count_markers_for(self, player, keys):
        # Create list of markers_in_row
        markers_in_row = [self.squares[key].marker for key in keys]
        # Return how many markers_in_row there are for that player
        return markers_in_row.count(player.marker)
    
    def find_empty_square(self, markers_in_row):
        empty_square_index = markers_in_row.index(Square.INITIAL_MARKER)
        return empty_square_index + 1

class Player:
    def __init__(self, marker):
        self.marker = marker

class Human(Player):
    def __init__(self):
        super().__init__(Square.HUMAN_MARKER)

class Computer(Player):
    def __init__(self):
        super().__init__(Square.COMPUTER_MARKER)

class TTTGame:
    POSSIBLE_WINNING_ROWS = (
        (1, 2, 3),  # top row of board
        (4, 5, 6),  # center row of board
        (7, 8, 9),  # bottom row of board
        (1, 4, 7),  # left column of board
        (2, 5, 8),  # middle column of board
        (3, 6, 9),  # right column of board
        (1, 5, 9),  # diagonal: top-left to bottom-right
        (3, 5, 7),  # diagonal: top-right to bottom-left
    )

    def __init__(self):
        self.board = Board()
        self.human = Human()
        self.computer = Computer()

    def play(self):
        self.display_welcome_message()
        while True:
            while True:
                self.board.display()

                self.human_moves()
                self.board.display() # Delete when not needed
                if self.is_game_over():
                    break

                self.computer_moves()
                if self.is_game_over():
                    break

                # clear_screen()

            self.board.display()
            self.display_results()

            if self.play_again() == 'n':
                break

            self.board.reset() # The suggested solution puts this at the top of the loop. Is it OK here?

        self.display_goodbye_message()

    def play_again(self):
        while True:
            player_input = input('Would you like to play again? Enter y or n. ').lower()

            if player_input in ('y', 'n'):
                break

            print("Sorry, that's not a valid response.")
        
        return player_input
        
    def display_welcome_message(self):
        print("Welcome to Tic Tac Toe!")

    def display_goodbye_message(self):
        print("Thanks for playing Tic Tac Toe! Goodbye!")

    def display_results(self):
        if self.is_winner(self.human):
            print("You won! Congratulations!")
        elif self.is_winner(self.computer):
            print("I won! I won! Take that, human!")
        else:
            print("A tie game. How boring.")

    def join_or(self, valid_choices, delimiter=", ", word='or'):
        choices_list = [str(choice) for choice in valid_choices]
        initial_choices_str = delimiter.join(choices_list[:-1])

        return f'{initial_choices_str} {word} {choices_list[-1]}'

    def human_moves(self):
        valid_choices = self.board.unused_squares()
        while True:
            prompt = f"Choose a square {self.join_or(valid_choices)}: "
            choice = input(prompt)

            try:
                choice = int(choice)
                if choice in valid_choices:
                    break
            except ValueError:
                pass

            print("Sorry, that's not a valid choice.")
            print()

        self.board.mark_square_at(choice, self.human.marker)

    def get_squares_in_row(self, row):
        squares_in_row = {square: self.board.squares[square].marker 
                for square in row}

        markers_in_row = list(squares_in_row.values())

        return squares_in_row, markers_in_row
    
    # TODO: move this into the Player class? Will need to update self.computer.marker on last line. Also - how to access the board
    def place_marker(self, squares_in_row):
                empty_square = [position 
                                for position, marker in squares_in_row.items() 
                                if marker == Square.INITIAL_MARKER]
                
                self.board.mark_square_at(empty_square[0], self.computer.marker)

    def computer_moves(self):
        computer_has_moved = False

        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            squares_in_row, markers_in_row = self.get_squares_in_row(row)

            number_of_computer_markers = markers_in_row.count(Square.COMPUTER_MARKER)

            if number_of_computer_markers == 2:
                if Square.INITIAL_MARKER in markers_in_row:
                    self.place_marker(squares_in_row)
                
                    print(f'Comp has moved aggressively.')
                    
                    computer_has_moved = True
                    break
            
        if computer_has_moved == False:
            for row in TTTGame.POSSIBLE_WINNING_ROWS:
                squares_in_row, markers_in_row = self.get_squares_in_row(row)

                number_of_human_markers = markers_in_row.count(Square.HUMAN_MARKER) # NOTE: Creates dependency with Square
                if number_of_human_markers == 2:
                # If the third square in the row is empty
                    if Square.INITIAL_MARKER in markers_in_row:
                        self.place_marker(squares_in_row)
                       
                        print(f'Comp has moved defensively.')
                        computer_has_moved = True
                        break

        if computer_has_moved == False:
            valid_choices = self.board.unused_squares()
            choice = random.choice(valid_choices)
            self.board.mark_square_at(choice, self.computer.marker)
            print('Comp has moved randomly')

    def is_game_over(self):
        return self.board.is_full() or self.someone_won()

    def three_in_a_row(self, player, row):
        return self.board.count_markers_for(player, row) == 3

    def someone_won(self):
        return (self.is_winner(self.human) or
                self.is_winner(self.computer))

    def is_winner(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.three_in_a_row(player, row):
                return True

        return False

game = TTTGame()
game.play()