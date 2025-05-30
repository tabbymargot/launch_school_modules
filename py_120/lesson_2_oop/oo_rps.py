import random

class Move:
    WINNING_MOVES = {
        'rock': ['scissors', 'lizard'],
        'paper': ['rock', 'spock'],
        'scissors': ['paper', 'lizard'],
        'lizard': ['paper', 'spock'],
        'spock': ['scissors', 'rock']
    }

    def __init__(self, name):
        self._name = name

    def _is_winning_move(self, player_move):
        return player_move in self.WINNING_MOVES[self._name]

class Rock(Move):
    def __init__(self, name):
        super().__init__(name)
    
class Paper(Move):
    def __init__(self, name):
        super().__init__(name)

class Scissors(Move):
    def __init__(self, name):
        super().__init__(name)
    
class Lizard(Move):
    def __init__(self, name):
        super().__init__(name)

class Spock(Move):
    def __init__(self, name):
        super().__init__(name)

class Player:
    CHOICES = ('rock', 'paper', 'scissors', 'lizard', 'spock')

    def __init__(current_player_instance):
        current_player_instance.move = None
        current_player_instance.score = 0

    def update_score(current_player_instance):
        current_player_instance.score += 1

    def reset_score(current_player_instance):
        current_player_instance.score = 0

class Computer(Player):
    def __init__(current_computer_instance): # Note that the code runs even if __init__ isn't
                        # defined here, as __init__ from the Player class
                        # is defaulted to.
        super().__init__()
        current_computer_instance.move = None

    def choose(current_computer_instance):
        current_computer_instance.move = random.choice(Player.CHOICES)

class Human(Player):
    def __init__(current_human_instance):
        super().__init__()
        current_human_instance.move = None

    def choose(current_human_instance):
        prompt = 'Please choose rock, paper, scissors, lizard or spock: '

        while True:
            choice = input(prompt).lower()
            if choice.lower() in Player.CHOICES:
                break

            print(f'Sorry, {choice} is not valid')

        current_human_instance.move = choice

class RPSGame:
    WINNING_SCORE = 3

    # Each of the values in this dictionary is a class.
    MOVES = {
        'rock': Rock,
        'paper': Paper,
        'scissors': Scissors, 
        'lizard': Lizard,
        'spock': Spock,
    }

    def __init__(current_rpsgame_instance):
        current_rpsgame_instance._human = Human()
        current_rpsgame_instance._computer = Computer()

    def _display_welcome_message(current_rpsgame_instance):
        print('Welcome to Rock Paper Scissors Lizard Spock!')

    def _human_wins(current_rpsgame_instance):
        human_move = current_rpsgame_instance._human.move # human_move references the move
        computer_move = current_rpsgame_instance._computer.move

        for move, move_class in RPSGame.MOVES.items():
            if human_move == move:
                # Instantiates the Move object, passing in the move which will become its name attribute. The Move object then invokes _is_winning_move().
                return move_class(move)._is_winning_move(computer_move)
        
    def _computer_wins(current_rpsgame_instance):
        human_move = current_rpsgame_instance._human.move
        computer_move = current_rpsgame_instance._computer.move

        for move, move_class in RPSGame.MOVES.items():
            if computer_move == move:
                return move_class(move)._is_winning_move(human_move)

    def _display_winner(current_rpsgame_instance):
        print(f'You chose: {current_rpsgame_instance._human.move}')
        print(f'The computer chose: {current_rpsgame_instance._computer.move}')

        if current_rpsgame_instance._human_wins():
            print('You win!')
            current_rpsgame_instance._human.update_score()
        elif current_rpsgame_instance._computer_wins():
            print('Computer wins!')
            current_rpsgame_instance._computer.update_score()
        else:
            print("It's a tie")

        print(f'Human score: {current_rpsgame_instance._human.score}')
        print(f'Computer score: {current_rpsgame_instance._computer.score}')

    def _display_overall_winner(current_rpsgame_instance):
        if current_rpsgame_instance._human.score == 3:
            print('You are the overall winner!')
        else:
            print('The computer is the overall winner!')

    def _play_again(current_rpsgame_instance):
        answer = input('Would you like to play again? (y/n) ')
        return answer.lower().startswith('y')

    def _display_goodbye_message(current_rpsgame_instance):
        print('Thanks for playing Rock Paper Scissors Lizard Spock. Goodbye!')

    def play(current_rpsgame_instance):
        current_rpsgame_instance._display_welcome_message()

        while True:
            while current_rpsgame_instance._human.score < 3 and current_rpsgame_instance._computer.score < 3:
                current_rpsgame_instance._human.choose() 
                current_rpsgame_instance._computer.choose()
                current_rpsgame_instance._display_winner()

            current_rpsgame_instance._display_overall_winner()

            if not current_rpsgame_instance._play_again(): # This method is part of the orchestration of the game, so makes sense to define it inside this RPSGame class.
                break

            current_rpsgame_instance._human.reset_score()
            current_rpsgame_instance._computer.reset_score()

        current_rpsgame_instance._display_goodbye_message()

RPSGame().play()

# print(RPSGame().WINNING_MOVES)