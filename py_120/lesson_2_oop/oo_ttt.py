class Square:
    def __init__(self):
        # STUB
        # We need some way to keep track of this square's
        #   marker.
        pass

class Board:
    def __init__(self):
        # STUB
        # We need a way to model the 3x3 grid. Perhaps
        #   "squares"?
        # What data structure should we use? A list? A
        #   dictionary? Something else?
        # What should the data structure store? Strings?
        #   Numbers? Square objects?
        pass

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
    def play(self):
        # SPIKE
        self.display_welcome_message()

        while True:
            self.display_board()

            self.first_player_moves()
            if self.is_game_over():
                break

            self.second_player_moves()
            if self.is_game_over():
                break

            break   # Execute loop only once for now

        self.display_board()
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
        # STUB
        # Display the board, including its current state.
        pass

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