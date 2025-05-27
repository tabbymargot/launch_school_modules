import random

class Move:
    WINNING_MOVES = {
        'rock': ['scissors', 'lizard'],
        'paper': ['rock', 'spock'],
        'scissors': ['paper', 'lizard'],
        'lizard': ['paper', 'spock'],
        'spock': ['scissors', 'rock']
    }

    def __init__(current_move_instance):
        pass

    def _is_winning_move(current_move_instance, player_move):
        return player_move in current_move_instance.WINNING_MOVES[current_move_instance._name]

class Rock(Move):
    def __init__(current_rock_instance):
        current_rock_instance._name = 'rock'
    
class Paper(Move):
    def __init__(current_paper_instance):
        super().__init__()
        current_paper_instance._name = 'paper'

class Scissors(Move):
    def __init__(current_scissors_instance):
        super().__init__()
        current_scissors_instance._name = 'scissors'
    
class Lizard(Move):
    def __init__(current_lizard_instance):
        super().__init__()
        current_lizard_instance._name = 'lizard'

class Spock(Move):
    def __init__(current_spock_instance):
        super().__init__()
        current_spock_instance._name = 'spock'

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

    def __init__(current_rpsgame_instance):
        current_rpsgame_instance._human = Human()
        current_rpsgame_instance._computer = Computer()
        current_rpsgame_instance._move = Move()
        current_rpsgame_instance._rock = Rock()
        current_rpsgame_instance._paper = Paper()
        current_rpsgame_instance._scissors = Scissors()
        current_rpsgame_instance._lizard = Lizard()
        current_rpsgame_instance._spock = Spock()

    def _display_welcome_message(current_rpsgame_instance):
        print('Welcome to Rock Paper Scissors Lizard Spock!')

    def _human_wins(current_rpsgame_instance):
        human_move = current_rpsgame_instance._human.move # human_move references the move
        computer_move = current_rpsgame_instance._computer.move
        
        if human_move == 'rock':
            return current_rpsgame_instance._rock._is_winning_move(computer_move)
        elif human_move == 'paper':
            return current_rpsgame_instance._paper._is_winning_move(computer_move)
        elif human_move == 'scissors':
            return current_rpsgame_instance._scissors._is_winning_move(computer_move)
        elif human_move == 'lizard':
            return current_rpsgame_instance._lizard._is_winning_move(computer_move)
        elif human_move == 'spock':
            return current_rpsgame_instance._spock._is_winning_move(computer_move)
        
    def _computer_wins(current_rpsgame_instance):
        human_move = current_rpsgame_instance._human.move
        computer_move = current_rpsgame_instance._computer.move

        if computer_move == 'rock':
            return current_rpsgame_instance._rock._is_winning_move(human_move)
        elif computer_move == 'paper':
            return current_rpsgame_instance._paper._is_winning_move(human_move)
        elif computer_move == 'scissors':
            return current_rpsgame_instance._scissors._is_winning_move(human_move)
        elif computer_move == 'lizard':
            return current_rpsgame_instance._lizard._is_winning_move(human_move)
        elif computer_move == 'spock':
            return current_rpsgame_instance._spock._is_winning_move(human_move)

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