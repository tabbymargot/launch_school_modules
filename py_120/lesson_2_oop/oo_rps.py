import random

class Player:
    CHOICES = ('rock', 'paper', 'scissors')

    def __init__(self):
        self.move = None
        self.score = 0

    def update_score(self):
        self.score += 1

    def reset_score(self):
        self.score = 0

class Computer(Player):
    def __init__(self): # Note that the code runs even if __init__ isn't
                        # defined here, as __init__ from the Player class
                        # is defaulted to.
        super().__init__()

    def choose(self):
        self.move = random.choice(Player.CHOICES)

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        prompt = 'Please choose rock, paper, or scissors: '

        while True:
            choice = input(prompt).lower()
            if choice.lower() in Player.CHOICES:
                break

            print(f'Sorry, {choice} is not valid')

        self.move = choice

class RPSGame:
    WINNING_SCORE = 3

    def __init__(self):
        self._human = Human()
        self._computer = Computer()

    def _display_welcome_message(self):
        print('Welcome to Rock Paper Scissors!')

    def _human_wins(self):
        human_move = self._human.move # human_move references the move
        # attribute belonging to the human object, but move is not in
        # itself an attribute of the RPSGame object.
        computer_move = self._computer.move

        return ((human_move == 'rock' and computer_move == 'scissors') or
                (human_move == 'paper' and computer_move == 'rock') or
                (human_move == 'scissors' and computer_move == 'paper'))

    def _computer_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return ((computer_move == 'rock' and human_move == 'scissors') or
                (computer_move == 'paper' and human_move == 'rock') or
                (computer_move == 'scissors' and human_move == 'paper'))

    def _display_winner(self):
        print(f'You chose: {self._human.move}')
        print(f'The computer chose: {self._computer.move}')

        if self._human_wins():
            print('You win!')
            self._human.update_score()
        elif self._computer_wins():
            print('Computer wins!')
            self._computer.update_score()
        else:
            print("It's a tie")

        print(f'Human score: {self._human.score}')
        print(f'Computer score: {self._computer.score}')

    def _display_overall_winner(self):
        if self._human.score == 3:
            print('You are the overall winner!')
        else:
            print('The computer is the overall winner!')

    def _play_again(self):
        answer = input('Would you like to play again? (y/n) ')
        return answer.lower().startswith('y')

    def _display_goodbye_message(self):
        print('Thanks for playing Rock Paper Scissors. Goodbye!')

    def play(self):
        self._display_welcome_message()

        while True:
            while self._human.score < 3 and self._computer.score < 3:
                self._human.choose() # The value of self._human (a Player object) is now a collaborator object of the RPSGame object (because an instance of RPSGame has called choose() on it).Previously it was just stored data.
                self._computer.choose()
                self._display_winner()

            self._display_overall_winner()

            if not self._play_again(): # This method is part of the orchestration of the game, so makes sense to define it inside this RPSGame class.
                break

            self._human.reset_score()
            self._computer.reset_score()

        self._display_goodbye_message()

RPSGame().play()