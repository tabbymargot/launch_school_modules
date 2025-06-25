""" 
PROBLEM
Restate in my words
Get number. Check validity. Tell player if too high or too low. Only allow 7 guesses

Inputs 
- User input (number)
Outputs
- Error message
- Messages to user:
    - too high / low
    - you won / lost

EXPLICIT / IMPLICIT REQUIREMENTS
- Invalid guesses don't count as a go

Clarifying questions

Edge cases
- Floats?

DATA STRUCTURES
Range?
ALGORITHM - STFC
High level
Create a valid range. Get user input and check if it's inside the range. If it's not, output error messgae and get new imput. If it is, output message too high / too low / correct number / out of guesses
Alternative High Level?
Actual algorithm
- Init instance variable remaining_guesses
- Init instance variable valid_range
- Init instance variable target_number (generate randomly)

- Outer loop:
- Output 
    "You have {remaining_guesses} guesses remaining."
    "Enter a number between 1 and 100:

    Inner Loop:
        - Get user input and assign to variable player_guess
        - Try / except block to check if input is valid. If it's not, output error messages as necessary
        - Continue looping until valid input obtained
        - Break if input is valid

- Compare player_guess with target_number.
    - If it's too high, output message 'too high' and reduce remaining_guesses by one.
    - If it's too low, output message 'too low' and reduce remaining_guesses by one.
    - Else - output message for correct number and end the game (break out of loop?)

"""
import random

class GuessingGame:
    def __init__(self):
        self.remaining_guesses = None
        self.valid_range = range(1, 100)
        self.target_number = None
        self.player_guess = None
        
    def validate_guess(self):
        print(repr(self.player_guess))
        # while True:
        #     if type(self.player_guess) != int:
        #         self.player_guess = input(
        #             "That's not a valid number! Please try again. \n"
        #             )
        #     elif self.player_guess not in self.valid_range:
        #         self.player_guess = input(
        #             "Invalid guess. Enter a number between 1 and 100. \n"
        #             )
        #     else:
        #         break

        while True:
            try: 
                self.player_guess = int(self.player_guess)
            except:
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
        self.remaining_guesses = 7
        self.target_number = random.choice(self.valid_range)

        while self.remaining_guesses > 0:
            print(f"You have {self.remaining_guesses} guesses remaining.")

            self.player_guess = (input("Enter a number between 1 and 100: \n"))
            
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

game = GuessingGame()
game.play()