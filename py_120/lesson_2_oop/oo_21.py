import random

class Card:
    def __init__(self):
        # STUB
        # What attributes does a card need? Rank? Suit?
        #   Points?
        pass

class Hand:
    def __init__(self):
        self.cards = []

class Deck:
    VALUES_AS_STRINGS = (['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'])

    ALL_CARDS = {
        'Clubs': VALUES_AS_STRINGS,
        'Diamonds': VALUES_AS_STRINGS,
        'Hearts': VALUES_AS_STRINGS,
        'Spades': VALUES_AS_STRINGS,
        }

    INTEGER_VALUES = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10,
    }
    def __init__(self):
        self.cards = []

        for suit, values in self.ALL_CARDS.items():
            for value in values:
                card = [suit, value]
                self.cards.append(card)

        # print(self.cards)  

class Participant:
    def __init__(self):
        # STUB
        # What attributes does a participant require? Score?
        #   Hand? Betting balance?
        # What else goes here? all the redundant behaviors
        #   from Player and Dealer?
        self.hand = Hand()

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

class Player(Participant):
    def __init__(self):
        super().__init__()
    
class Dealer(Participant):
    INITIAL_DEAL = 2

    def __init__(self):
        super().__init__()

    def deal(self, deck, participant):
        # random.shuffle(deck.cards)
        print(participant.hand.cards)
        
        for _ in range(self.INITIAL_DEAL):
            card = deck.cards[0]
            participant.hand.cards.append(card)
            deck.cards.remove(card)
            print(card in deck.cards)

        # print(participant.hand.cards)

        # if len(participant.hand.cards) == 1:
        #     return participant.hand.cards[0]

        # return participant.hand
        
    def hide(self):
        # STUB
        pass

    def reveal(self):
        # STUB
        pass

class TwentyOneGame:
    def __init__(self):
        # STUB
        # What attributes does the game need? A deck? Two
        #   participants?
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()

    def display_welcome_message(self):
        print("Welcome to 21!")

    def start(self):
        # SPIKE
        self.display_welcome_message()

        # TODO: When the program starts, give the player 5 dollars with which to bet. Deduct 1 dollar each time she loses, and add 1 dollar each time she wins. The program should quit when she is broke (0 dollars) or rich (has a total of 10 dollars).

        # TODO: WHILE player wants to continue
        # TODO: Be prepared to run out of cards. You can either create a new deck for each game, or keep track of how many cards remain and create a new deck as needed.

        self.deal_cards(self.player)
        print(self.player.hand.cards)

        self.deal_cards(self.dealer)
        print(self.dealer.hand.cards)

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

    def deal_cards(self, participant):
        self.dealer.deal(self.deck, participant)

    # def deal_dealers_cards(self):
    #     self.dealer.deal(self.deck, self.dealer)

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