# TODO: make the deck a collaborator object of Dealer rather than passing it in as an argument to the various methods?

# TODO: check no methods return a value and also have side effects
import json
with open('oo_21.json', 'r') as file:
    MESSAGES = json.load(file)

import os
import random

class Card:
    def __init__(self):
        self.suit = None
        self.str_value = None
        self.score = None

    @property
    def suit(self):
        return self._suit
    
    @suit.setter
    def suit(self, suit):
        self._suit = suit

    @property
    def str_value(self):
        return self._str_value
    
    @str_value.setter
    def str_value(self, str_value):
        self._str_value = str_value

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        self._score = score

class Hand():
    #TODO: there are now 2 constants with the same name
    MAX_WINNING_SCORE = 21

    # most_recently_dealt_card = None

    def __init__(self):
        self.cards = []
        self.score = None
        self.all_cards_except_last = None
        self.most_recently_dealt_card = None
        # self.aces = []
        # self.non_aces = []
        # self.aces_score = None
        # self.non_aces_score = None
        # self.low_value_ace = None
        # self.high_value_ace = None

    @property
    def cards(self):
        return self._cards
    
    @cards.setter
    def cards(self, cards):
        self._cards = cards

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        self._score = score

    @property
    def all_cards_except_last(self):
        return self._all_cards_except_last
    
    @all_cards_except_last.setter
    def all_cards_except_last(self, all_cards_except_last):
        self._all_cards_except_last = all_cards_except_last

    @property
    def most_recently_dealt_card(self):
        return self._most_recently_dealt_card
    
    @most_recently_dealt_card.setter
    def most_recently_dealt_card(self, most_recently_dealt_card):
        self._most_recently_dealt_card = most_recently_dealt_card

    # @property
    # def aces(self):
    #     return self._aces
    
    # @aces.setter
    # def aces(self, aces):
    #     self._aces = aces

    # @property
    # def non_aces(self):
    #     return self._non_aces
    
    # @non_aces.setter
    # def non_aces(self, non_aces):
    #     self._non_aces = non_aces

    # @property
    # def aces_score(self):
    #     return self._aces_score
    
    # @aces_score.setter
    # def aces_score(self, aces_score):
    #     self._aces_score = aces_score

    # @property
    # def non_aces_score(self):
    #     return self._non_aces_score
    
    # @non_aces_score.setter
    # def non_aces_score(self, non_aces_score):
    #     self._non_aces_score = non_aces_score

    # @property
    # def low_value_ace(self):
    #     return self._low_value_ace
    
    # @low_value_ace.setter
    # def low_value_ace(self, low_value_ace):
    #     self._low_value_ace = low_value_ace

    # @property
    # def high_value_ace(self):
    #     return self._high_value_ace
    
    # @high_value_ace.setter
    # def high_value_ace(self, high_value_ace):
    #     self._high_value_ace = high_value_ace

    def calculate_value(self):
        aces = []
        non_aces = []

        for card in self.cards:
            if card.str_value == 'Ace':
                aces.append(card)
            else:
                non_aces.append(card)

        non_aces_score = sum([card.score for card in non_aces])

        aces_score = self.calculate_ace_values(aces, non_aces_score)

        self.score = non_aces_score + aces_score
    
    def calculate_ace_values(self, aces, non_aces_score):
        aces_values = []

        for ace in aces:
            low_value_ace = ace.score[0]
            high_value_ace = ace.score[1]

            if ((non_aces_score + sum(aces_values) + high_value_ace)
            <= self.MAX_WINNING_SCORE):
                aces_values.append(high_value_ace)

            elif ((non_aces_score + sum(aces_values) + low_value_ace)
            <= self.MAX_WINNING_SCORE):
                aces_values.append(low_value_ace)

            elif high_value_ace in aces_values:
                for idx, value in enumerate(aces_values):
                    if value == high_value_ace:
                        aces_values[idx] = low_value_ace
                        break

                aces_values.append(low_value_ace)

            else:
                pass

        return sum(aces_values)
    
    def get_details_of_all_cards_except_last(self):
        card_details = []

        for card in self.all_cards_except_last:
            suit = card.suit
            value = card.str_value
            card_details.append(f'the {value} of {suit}')

        return ', '.join([details for details in card_details])

    def get_last_dealt_card_details(self):
        suit = self.most_recently_dealt_card.suit
        value = self.most_recently_dealt_card.str_value

        return f'the {value} of {suit}'

class Deck:
    SUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
    STR_VALUES = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    SCORES = ((1, 11), 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)

    def __init__(self):
        self.cards = []

        # Create 52 card objects and add to a list, self.cards
        for suit in self.SUITS:
            values_and_scores = zip(self.STR_VALUES, self.SCORES)

            for str_value, score in values_and_scores:
                card = Card()
                card.suit = suit
                card.str_value = str_value
                card.score = score

                self.cards.append(card)

class Participant:
    MAX_WINNING_SCORE = 21

    def __init__(self):
        # STUB
        # What attributes does a participant require? Score?
        #   Hand? Betting balance?
        # What else goes here? all the redundant behaviors
        #   from Player and Dealer?
        self.hand = Hand()

    def is_busted(self):
        return self.hand.score > self.MAX_WINNING_SCORE


class Player(Participant):
    def __init__(self):
        super().__init__()
    
class Dealer(Participant):

    def __init__(self):
        super().__init__()
        self.deck = Deck()

    def deal(self, participant):
        random.shuffle(self.deck.cards)

        if len(participant.hand.cards) == 0:
            number_of_cards_to_deal = 2
        else:
            number_of_cards_to_deal = 1
        
        for _ in range(number_of_cards_to_deal):
            card = self.deck.cards[0]

            participant.hand.cards.append(card)
            self.deck.cards.remove(card)

            participant.hand.all_cards_except_last = participant.hand.cards[:-1]
            participant.hand.most_recently_dealt_card = participant.hand.cards[-1]
            

class TwentyOneGame:
    MAX_WINNING_SCORE = 21
    DEALER_MINIMUM_SCORE = 17

    def __init__(self):
        self.dealer = Dealer()
        self.player = Player()

    def prompt(self, message):
        print(f'==> {message}')

    def display_welcome_message(self):
        self.prompt("Welcome to 21!")

    def start(self):
        self.display_welcome_message()

        # TODO: When the program starts, give the player 5 dollars with which to bet. Deduct 1 dollar each time she loses, and add 1 dollar each time she wins. The program should quit when she is broke (0 dollars) or rich (has a total of 10 dollars).

        # TODO: WHILE player wants to continue
        # TODO: Be prepared to run out of cards. You can either create a new deck for each game, or keep track of how many cards remain and create a new deck as needed.

        self.dealer.deal(self.player)
        self.dealer.deal(self.dealer)

        self.player.hand.calculate_value()
        self.dealer.hand.calculate_value()

        self.show_cards()

        self.player_turn()

        # if self.player.hand.score > self.MAX_WINNING_SCORE:
        if self.player.is_busted():
            result = self.establish_result()
        else:
            self.dealer_turn()
            result = self.establish_result()

        self.display_result(result)

        # TODO: After each game is over, ask the player if they want to play again. Start a new game if they say yes, else end the game.

        self.display_goodbye_message()


    def show_cards(self):

        self.prompt(f"Your hand contains the {self.player.hand.get_details_of_all_cards_except_last()} and {self.player.hand.get_last_dealt_card_details()}.\n")
        # time.sleep(1)

        self.prompt(f"Your hand is worth {self.player.hand.score} points.\n")
        # time.sleep(1)

        self.prompt(f"One of the dealer's two cards is {self.dealer.hand.get_last_dealt_card_details()}.\n")
        # time.sleep(1)

    def player_turn(self):
        while True:
            player_move = self.get_player_move()

            # TODO: Move hit / stay to Participant class?
            if player_move == 'h':
                self.player_hit()

                # if self.player.hand.score > self.MAX_WINNING_SCORE:
                if self.player.is_busted():
                    break

                self.print_updated_player_score()
            else:
                break

    def get_player_move(self):
        while True:
            self.prompt("Would you like to hit or stay? Enter H for hit " \
            "and S for stay.\n")
            move = input().strip().lower()
            if move in ('h', 's'):
                return move

            self.prompt("That's not a valid choice. Please try again\n.")
            # time.sleep(1.5)

    def player_hit(self):
        os.system('clear')

        self.prompt('Dealing additional card...\n')
        # time.sleep(1)
        self.dealer.deal(self.player)
        self.print_updated_player_hand()
        self.player.hand.calculate_value()

    def print_updated_player_hand(self):
        self.prompt(f"Your hand now contains the {self.player.hand.get_details_of_all_cards_except_last()} and {self.player.hand.get_last_dealt_card_details()}.\n")

    def print_updated_player_score(self):
        self.prompt(f'Your new score is {self.player.hand.score}.\n')
        # time.sleep(1)

        self.prompt(f"As a reminder, one of the dealer's two " \
                f"cards is {self.dealer.hand.get_last_dealt_card_details()}.\n")
        # # time.sleep(1)

    def dealer_turn(self):
        # while self.dealer.hand.score <= self.MAX_WINNING_SCORE:
        while not self.dealer.is_busted():

            self.display_dealer_hand_info('Dealer hand')

            self.dealer.hand.calculate_value()

            if self.dealer.hand.score >= self.DEALER_MINIMUM_SCORE:
                break
            
            self. display_dealer_hand_info('Current score')

            self.dealer.deal(self.dealer)
            self.dealer.hand.calculate_value()
            
            self. display_dealer_hand_info('Latest card, updated score')

            # time.sleep(1)

    def display_dealer_hand_info(self, required_info):
        match required_info:
            case 'Dealer hand':
                self.prompt(f"The dealer's hand contains the {self.dealer.hand.get_details_of_all_cards_except_last()} and {self.dealer.hand.get_last_dealt_card_details()}.\n")
            case 'Current score':
                self.prompt(f"The dealer has {self.dealer.hand.score} points, so I'm just " \
                "dealing them another card...\n") 
            case 'Latest card, updated score':
                self.prompt(f"The dealer's new card is {self.dealer.hand.get_last_dealt_card_details()}.\n")

    def display_goodbye_message(self):
        print("Thanks for playing 21! Goodbye!")

    def establish_result(self):
        if self.player.hand.score > self.MAX_WINNING_SCORE:
            return 'player_bust'
        if self.dealer.hand.score > self.MAX_WINNING_SCORE:
            return 'dealer_bust'
        if self.player.hand.score > self.dealer.hand.score:
            return 'player_wins'
        if self.dealer.hand.score > self.player.hand.score:
            return 'dealer_wins'

        return 'tie'

    def display_result(self, result):
        player_score = self.player.hand.score
        dealer_score = self.dealer.hand.score

        if result != 'player_bust':
            self.prompt(MESSAGES['both_scores'].format(player_score=player_score, dealer_score=dealer_score))
            # time.sleep(1.5)

        match result:
            case 'player_bust':
                self.prompt(MESSAGES['new_score'].format(player_score=player_score))
                # time.sleep(1.5)

                self.prompt(MESSAGES['player_bust'])
                # time.sleep(1.5)

            case 'dealer_bust':
                self.prompt(MESSAGES['dealer_bust'])
                # time.sleep(1.5)

            case 'player_wins':
                self.prompt(MESSAGES['player_wins'])
                # time.sleep(1.5)

            case 'dealer_wins':
                self.prompt(MESSAGES['player_loses'])
                # time.sleep(1.5)

            case 'tie':
                self.prompt(MESSAGES['tie'])
                # time.sleep(1.5)

game = TwentyOneGame()
game.start()