class Square:
    INITIAL_MARKER = " "
    HUMAN_MARKER = "X"
    COMPUTER_MARKER = "O"

    def __init__(self, marker=INITIAL_MARKER):
        self.marker = marker

    def __str__(self):
        # Printing the square will now print its marker instead of the entire object. This is more helpful.
        return self.marker

class Board:
    def __init__(self):
        self.squares = {
            1: Square(),
            2: Square(),
            3: Square("X"), # testing -- remove "X" later
            4: Square(),
            5: Square("O"), # testing -- remove "O" later
            6: Square(),
            7: Square("X"), # testing -- remove "X" later
            8: Square(),
            9: Square(),
        }

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

class Row:
    def __init__(self):
        # STUB
        # We need some way to identify a row of 3 squares
        pass

class Marker:
    def __init__(self):
        # STUB
        # A marker is something that represents a board
        #   square that belongs to a particular player. That
        #   is, it's a square that was chosen by the player.
        pass

class Player:
    def __init__(self):
        # STUB
        # A player is either a human or a computer that is
        #   playing the game.
        # Perhaps we need a "marker" to keep track of this
        #   player's symbol? (i.e., 'X' or 'O')
        pass

    def mark(self):
        # STUB
        # We need a way to mark the board with this player's
        #   marker. How do we access the board?
        pass

    def play(self):
        # STUB
        # We need a way for each player to play the game.
        # Do we need access to the board?
        pass

class Human(Player):
    def __init__(self):
        # STUB
        # What does a human player need to do? How does it
        #   differ from the basic Player or a Computer?
        pass

class Computer(Player):
    def __init__(self):
        # STUB
        # What does a computer player need to do? How does
        #   it differ from the basic Player or a Human?
        pass

class TTTGame:
    def __init__(self):
      self.board = Board()
      
    def play(self):
        self.display_welcome_message()

        while True:
            self.board.display()

            self.first_player_moves()
            if self.is_game_over():
                break

            self.second_player_moves()
            if self.is_game_over():
                break

            break   # Execute loop only once for now

        self.board.display()
        self.display_results()
        self.display_goodbye_message()

    def display_welcome_message(self):
        print("Welcome to Tic Tac Toe!")

    def display_goodbye_message(self):
        print("Thanks for playing Tic Tac Toe! Goodbye!")

    def display_results(self):
        # STUB
        # Show the results of this game (win, lose, tie).
        pass

    def display_board(self):
        print()
        print("     |     |     ")
        print("  O  |     |  O  ")
        print("     |     |     ")
        print("-----+-----+-----")
        print("     |     |     ")
        print("     |  X  |     ")
        print("     |     |     ")
        print("-----+-----+-----")
        print("     |     |     ")
        print("  X  |     |     ")
        print("     |     |     ")
        print()

    def first_player_moves(self):
        # STUB
        # The first player makes a move.
        pass

    def second_player_moves(self):
        # STUB
        # The second player makes a move.
        pass

    def is_game_over(self):
        # STUB
        # We'll start by assuming the game never ends.
        return False

game = TTTGame()
game.play()

# _______________________
