class Card:
    def __init__(self):
        # STUB
        # What attributes does a card need? Rank? Suit?
        #   Points?
        pass

class Deck:
    def __init__(self):
        # STUB
        # What attributes does a deck need? A collection of
        #   52 cards?
        # Some data structure, like a list or dictionary,
        #   might be required.
        pass

    def deal(self):
        # STUB
        # Does the dealer or the deck deal the cards?
        pass

class Participant:
    def __init__(self):
        # STUB
        # What attributes does a participant require? Score?
        #   Hand? Betting balance?
        # What else goes here? all the redundant behaviors
        #   from Player and Dealer?
        pass

class Player(Participant):
    def __init__(self):
        # STUB
        # What additional attributes might a player need?
        # Score? Hand? Amount of money available?
        pass

    def hit(self):
        # STUB
        pass

    def stay(self):
        # STUB
        pass

    def is_busted(self):
        # STUB
        pass

    def score(self):
        # STUB
        pass

class Dealer(Participant):
    def __init__(self):
        # STUB
        # Very similar to a Player; do we need this?
        pass

    def hit(self):
        # STUB
        pass

    def stay(self):
        # STUB
        pass

    def is_busted(self):
        # STUB
        pass

    def score(self):
        # STUB
        pass

    def hide(self):
        # STUB
        pass

    def reveal(self):
        # STUB
        pass

    def deal(self):
        # STUB
        # Does the dealer or the deck deal?
        pass

class TwentyOneGame:
    def __init__(self):
        # STUB
        # What attributes does the game need? A deck? Two
        #   participants?
        pass

    def display_welcome_message(self):
        print("Welcome to 21!")

    def start(self):
        # SPIKE
        self.display_welcome_message()

        # TODO: When the program starts, give the player 5 dollars with which to bet. Deduct 1 dollar each time she loses, and add 1 dollar each time she wins. The program should quit when she is broke (0 dollars) or rich (has a total of 10 dollars).

        # TODO: WHILE player wants to continue
        # TODO: Be prepared to run out of cards. You can either create a new deck for each game, or keep track of how many cards remain and create a new deck as needed.

        self.deal_cards()

        self.show_cards()

        self.player_turn()

        self.dealer_turn()
            # The dealer doesn't play at all if the player busts.
            # Display the dealer's hand, including the hidden card, and report his point total.
            # Redisplay the dealer's hand and point total and each time he hits.
            # Display the results when the dealer stays.

        self.display_result()

        # TODO: After each game is over, ask the player if they want to play again. Start a new game if they say yes, else end the game.

        self.display_goodbye_message()

    def deal_cards(self):
        # STUB
        pass

    def show_cards(self):
        # STUB
        pass

    def player_turn(self):
        # STUB
        pass

    def dealer_turn(self):
        # STUB
        pass

    def display_goodbye_message(self):
        print("Thanks for playing 21! Goodbye!")

    def display_result(self):
        # STUB
        pass

game = TwentyOneGame()
game.start()