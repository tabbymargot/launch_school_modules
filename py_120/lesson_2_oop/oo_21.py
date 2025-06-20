# TODO: go through and look at how instance methods match the explanation here https://www.remnote.com/w/6810e016669adfcb7792a93f/IP3ToB70IwpvOGTV8
# TODO: add validation to getters and setters
# TODO: go through and determine the collaborator objects. Check with LSBot
import json
with open('oo_21.json', 'r') as file:
    MESSAGES = json.load(file)

import os
import random

MAX_WINNING_SCORE = 21
SUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
STR_VALUES = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
SCORES = ((1, 11), 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)

# SUITS_TEST = SUITS + ("InvalidSuit",)
# STR_VALUES_TEST = STR_VALUES + ["InvalidValue"]
# SCORES_TEST = SCORES + (99,)

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
        # if suit not in SUITS:
        #     print(f'Suit: {suit}')
        #     print("That's not a suit!")
        print(suit)
        self._suit = suit

    @property
    def str_value(self):
        return self._str_value
    
    @str_value.setter
    def str_value(self, str_value):
        # if str_value not in STR_VALUES:
        #     print(f'Str_value: {str_value}')
        #     print("That's not a valid string value!")
        
        print(str_value)
        self._str_value = str_value

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        # if score not in SCORES:
        #     print(f'Score: {score}')
        #     print("That's not a valid score!")
        
        print(score)
        self._score = score

class Hand():
    def __init__(self):
        self.cards = []
        self.score = None
        self.all_cards_except_last = None
        self.most_recently_dealt_card = None

    @property
    def cards(self):
        return self._cards
    
    @cards.setter
    def cards(self, cards):
        if not isinstance(cards, list):
            return "That's not a list of cards!"
        
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
            <= MAX_WINNING_SCORE):
                aces_values.append(high_value_ace)

            elif ((non_aces_score + sum(aces_values) + low_value_ace)
            <= MAX_WINNING_SCORE):
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
    def __init__(self):
        self.cards = []

    @property
    def cards(self):
        return self._cards
    
    @cards.setter
    def cards(self, cards):
        self._cards = cards 

        for suit in SUITS:
            values_and_scores = zip(STR_VALUES, SCORES)

            for str_value, score in values_and_scores:
                card = Card()
                card.suit = suit
                card.str_value = str_value
                card.score = score

                self.cards.append(card)

class Participant:

    def __init__(self):
        # STUB
        # What attributes does a participant require? Score?
        #   Hand? Betting balance?
        # What else goes here? all the redundant behaviors
        #   from Player and Dealer?
        self.hand = Hand()
    
    @property
    def hand(self):
        return self._hand
    
    @hand.setter
    def hand(self, hand):
        self._hand = hand

    def is_busted(self):
        return self.hand.score > MAX_WINNING_SCORE

class Player(Participant):
    def __init__(self):
        super().__init__()
    
class Dealer(Participant):

    def __init__(self):
        super().__init__()
        self._deck = Deck()

    def deal(self, participant):
        random.shuffle(self._deck.cards)

        if len(participant.hand.cards) == 0:
            number_of_cards_to_deal = 2
        else:
            number_of_cards_to_deal = 1
        
        for _ in range(number_of_cards_to_deal):
            card = self._deck.cards[0]
            
            #TODO: how does this work with the setter method? Is the error message appropriate?
            participant.hand.cards.append(card)
            self._deck.cards.remove(card)

            participant.hand.all_cards_except_last = participant.hand.cards[:-1]
            participant.hand.most_recently_dealt_card = participant.hand.cards[-1]
            
class TwentyOneGame:
    DEALER_MINIMUM_SCORE = 17

    def __init__(self):
        self._dealer = Dealer()
        self._player = Player()

    def prompt(self, message):
        print(f'==> {message}')

    def display_welcome_message(self):
        self.prompt("Welcome to 21!")

    def start(self):
        self.display_welcome_message()

        # TODO: When the program starts, give the player 5 dollars with which to bet. Deduct 1 dollar each time she loses, and add 1 dollar each time she wins. The program should quit when she is broke (0 dollars) or rich (has a total of 10 dollars).

        # TODO: WHILE player wants to continue
        # TODO: Be prepared to run out of cards. You can either create a new deck for each game, or keep track of how many cards remain and create a new deck as needed.

        self._dealer.deal(self._player)
        self._dealer.deal(self._dealer)

        self._player.hand.calculate_value()
        self._dealer.hand.calculate_value()

        self.show_cards()

        self.player_turn()

        if self._player.is_busted():
            result = self.establish_result()
        else:
            self.dealer_turn()
            result = self.establish_result()

        self.display_result(result)

        # TODO: After each game is over, ask the player if they want to play again. Start a new game if they say yes, else end the game.

        self.display_goodbye_message()

    def show_cards(self):

        # self.prompt(MESSAGES['_player_hand_contains'].format(all_but_last_card=all_but_last_card, last_card=last_card))

        self.prompt(f"Your hand contains the {self._player.hand.get_details_of_all_cards_except_last()} and {self._player.hand.get_last_dealt_card_details()}.\n")
        # time.sleep(1)

        self.prompt(f"Your hand is worth {self._player.hand.score} points.\n")
        # time.sleep(1)

        self.prompt(f"One of the dealer's two cards is {self._dealer.hand.get_last_dealt_card_details()}.\n")
        # time.sleep(1)

    def player_turn(self):
        while True:
            player_move = self.get_player_move()

            if player_move == 'h':
                self.player_hit()

                if self._player.is_busted():
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
        self._dealer.deal(self._player)
        self.print_updated_player_hand()
        self._player.hand.calculate_value()

    def print_updated_player_hand(self):
        self.prompt(f"Your hand now contains the {self._player.hand.get_details_of_all_cards_except_last()} and {self._player.hand.get_last_dealt_card_details()}.\n")

    def print_updated_player_score(self):
        self.prompt(f'Your new score is {self._player.hand.score}.\n')
        # time.sleep(1)

        self.prompt(f"As a reminder, one of the dealer's two " \
                f"cards is {self._dealer.hand.get_last_dealt_card_details()}.\n")
        # # time.sleep(1)

    def dealer_turn(self):
        while not self._dealer.is_busted():
            self.display_dealer_hand_info('Dealer hand')

            self._dealer.hand.calculate_value()

            if self._dealer.hand.score >= self.DEALER_MINIMUM_SCORE:
                break
            
            self.display_dealer_hand_info('Current score')

            self._dealer.deal(self._dealer)
            self._dealer.hand.calculate_value()
            
            self. display_dealer_hand_info('Latest card, updated score')

            # time.sleep(1)

    def display_dealer_hand_info(self, required_info):
        match required_info:
            case 'Dealer hand':
                self.prompt(f"The dealer's hand contains the {self._dealer.hand.get_details_of_all_cards_except_last()} and {self._dealer.hand.get_last_dealt_card_details()}.\n")
            case 'Current score':
                self.prompt(f"The dealer has {self._dealer.hand.score} points, so I'm just " \
                "dealing them another card...\n") 
            case 'Latest card, updated score':
                self.prompt(f"The dealer's new card is {self._dealer.hand.get_last_dealt_card_details()}.\n")

    def display_goodbye_message(self):
        print("Thanks for playing 21! Goodbye!")

    def establish_result(self):
        # TODO: instead of returning a value, create a result attribute? Would need to update the display_result function too.
        if self._player.hand.score > MAX_WINNING_SCORE:
            return 'player_bust'
        
        if self._dealer.hand.score > MAX_WINNING_SCORE:
            return 'dealer_bust'
        
        if self._player.hand.score > self._dealer.hand.score:
            return 'player_wins'
        
        if self._dealer.hand.score > self._player.hand.score:
            return 'dealer_wins'

        return 'tie'

    def display_result(self, result):
        player_score = self._player.hand.score
        dealer_score = self._dealer.hand.score

        if result != 'player_bust':
            self.prompt(MESSAGES['both_scores'].format(player_score=player_score, dealer_score=dealer_score))
            # time.sleep(1.5)
        # TODO: update the MESSAGES strings so that they're different from the strings following the case statements
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