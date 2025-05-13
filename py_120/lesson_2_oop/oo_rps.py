import random

class Player:
    CHOICES = ('rock', 'paper', 'scissors')

    def __init__(self, player_type):
        self._player_type = player_type.lower() # stores state that distinguishes the players. 
        self.move = None # this attribute will be updated in the choose() method. But it's good practice to initialise it in init, so that we can get an overview of all the instance variables an instance will have. Notice also that it's PUBLIC.

    def _is_human(self):
        return self._player_type == 'human'

    def choose(self): # a PUBLIC method since we'll be calling it from inside the RPSGame class
        if self._is_human():
            prompt = 'Please choose rock, paper, or scissors: '

            while True:
                choice = input(prompt).lower()
                if choice in Player.CHOICES:
                    break

                print(f'Sorry, {choice} is not valid')

            self.move = choice
        else:
            self.move = random.choice(Player.CHOICES)


class Move: 
    def __init__(self):
        # This seems like we need something to keep track
        # of the choice... a move object can be "paper", "rock" or "scissors"
        pass

class Rule:
    def __init__(self):
        # not sure what the "state" of a rule object should be
        pass

    # not sure where "compare" goes yet
    def compare(self, move1, move2):
        pass

class RPSGame:
    def __init__(self):
        self._human = Player('human') # Player is instantiated from inside this class (instead of inside the Player class) to follow the principle of dependency direction - RPSGame depends on Players, but Players don't depend on RPSGame - this is covered later in PY120
        self._computer = Player('computer')

    def _display_welcome_message(self):
        print('Welcome to Rock Paper Scissors!')

    def _display_winner(self):
        human_move = self._human.move
        computer_move = self._computer.move

        print(f'You chose: {human_move}')
        print(f'The computer chose: {computer_move}')

        if ((human_move == 'rock' and computer_move == 'scissors') or
            (human_move == 'paper' and computer_move == 'rock') or
            (human_move == 'scissors' and computer_move == 'paper')):

            print('You win!')
        elif ((computer_move == 'rock' and human_move == 'scissors') or
            (computer_move == 'paper' and human_move == 'rock') or
            (computer_move == 'scissors' and human_move == 'paper')):

            print('Computer wins!')
        else:
            print("It's a tie")

    def _play_again(self):
        answer = input('Would you like to play again? (y/n) ')
        return answer.lower().startswith('y')
    
    def _display_goodbye_message(self):
        print('Thanks for playing Rock Paper Scissors. Goodbye!')

    def play(self):
        self._display_welcome_message()

        while True:
            self._human.choose() # The value of self._human (a Player object) is now a collaborator object of the RPSGame object (because an instance of RPSGame has called choose() on it). Previously (line 47) it was just stored data.
            self._computer.choose()
            self._display_winner()

            if not self._play_again(): # This method is part of the orchestration of the game, so makes sense to define it inside this RPSGame class.
                break

        self._display_goodbye_message()

RPSGame().play()