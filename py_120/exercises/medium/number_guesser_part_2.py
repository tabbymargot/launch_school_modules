import math
import random

class GuessingGame:
    def __init__(self, low, high):
        # self.remaining_guesses = None
        self.high_end = high
        self.low_end = low
        self.remaining_guesses = int(math.log2(self.high_end - self.low_end + 1)) + 1
        self.valid_range = range(self.low_end, self.high_end + 1)
        self.target_number = None
        self.player_guess = None
        
    def validate_guess(self):
        while True:
            try: 
                self.player_guess = int(self.player_guess)
            except ValueError:
                self.player_guess = input("That's not a valid number! Please try again. \n")
            else:
                if self.player_guess in self.valid_range:
                    break    
                else:
                    self.player_guess = input("Invalid guess. Enter a number between 1 and 100 \n")

    def output_player_update(self):
        if self.player_guess < self.target_number:
            print('Your guess is too low.\n')
        else:
            print('Your guess is too high.\n')

    def play_one_game(self):
        # self.remaining_guesses = 7
        self.target_number = random.choice(self.valid_range)

        while self.remaining_guesses > 0:
            print(f"You have {self.remaining_guesses} guesses remaining.")

            self.player_guess = (input(f"Enter a number between {self.low_end} and {self.high_end}: \n"))
            
            self.validate_guess()

            if self.player_guess != self.target_number:
                self.output_player_update()
            else:
                print("That's the number!\n\nYou won!")
                break
            
            self.remaining_guesses -= 1

            if self.remaining_guesses == 0:
                print('You have no more guesses. You lost!\n')

    def play(self):
        while True:
            self.play_one_game()

game = GuessingGame(501, 1500)
game.play()