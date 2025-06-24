# TODO: go through and determine the collaborator objects. Check with LSBot
import json
with open('oo_21.json', 'r') as file:
    MESSAGES = json.load(file)

import os
import random
import time

SUITS             = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
STR_VALUES        = (['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                    'Jack', 'Queen', 'King'])
SCORES            =  ((1, 11), 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)
MAX_WINNING_SCORE = 21
MIN_BANKROLL = 0
MAX_BANKROLL = 15

class Card:
    def __init__(self):
        self._initializing = True
        self.suit = None
        self.str_value = None
        self.score = None
        self._initializing = False

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, suit):
        if not self._initializing and suit not in SUITS:
            raise ValueError(
                "Suit must be one of the following strings: " \
                "Clubs, Diamonds, Hearts or Spades"
                )

        self._suit = suit

    @property
    def str_value(self):
        return self._str_value

    @str_value.setter
    def str_value(self, str_value):
        if not self._initializing and str_value not in STR_VALUES:
            raise ValueError("Invalid string value")

        self._str_value = str_value

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if not self._initializing and score not in SCORES:
            raise ValueError("Invalid card score.")

        self._score = score

class Hand():
    def __init__(self):
        self._initializing = True
        self.cards = []
        self.score = 0
        self.all_cards_except_last = []
        self.most_recently_dealt_card = None
        self._initializing = False

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, cards):
        if not self._initializing and not isinstance(cards, list):
            raise TypeError("The hand's card attribute must be a list")

        self._cards = cards

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise TypeError("The hand's score attribute must be an integer")

        self._score = score

    @property
    def all_cards_except_last(self):
        return self._all_cards_except_last

    @all_cards_except_last.setter
    def all_cards_except_last(self, all_cards_except_last):
        if  not isinstance(all_cards_except_last, list):
            raise TypeError(
                "The hand's all_cards_except_last attribute must be a list"
                )

        self._all_cards_except_last = all_cards_except_last

    @property
    def most_recently_dealt_card(self):
        return self._most_recently_dealt_card

    @most_recently_dealt_card.setter
    def most_recently_dealt_card(self, most_recently_dealt_card):
        if  not self._initializing and \
            not isinstance(most_recently_dealt_card, Card):
            raise TypeError(
                "The hand's most_recently_dealt_card attribute must be a Card"
                )

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

    def ace_should_be_high(self, non_aces_score, aces_values, high_value_ace):
        return ((non_aces_score + sum(aces_values) + high_value_ace)
        <= MAX_WINNING_SCORE)
    
    def ace_should_be_low(self, non_aces_score, aces_values, low_value_ace):
        return ((non_aces_score + sum(aces_values) + low_value_ace)
        <= MAX_WINNING_SCORE)

    def calculate_ace_values(self, aces, non_aces_score):
        aces_values = []

        for ace in aces:
            low_value_ace = ace.score[0]
            high_value_ace = ace.score[1]

            if self.ace_should_be_high(non_aces_score, aces_values, high_value_ace):
                aces_values.append(high_value_ace)

            elif self.ace_should_be_low(non_aces_score, aces_values, low_value_ace):
                aces_values.append(low_value_ace)

            else:
                pass

        return sum(aces_values)

    def get_details_of_all_cards_except_last(self):
        all_card_details = []

        print(f'Type: {type(self.all_cards_except_last)}')

        for card in self.all_cards_except_last:
            suit = card.suit
            value = card.str_value
            all_card_details.append(f'the {value} of {suit}')

        return ', '.join(list(all_card_details))

    def get_last_dealt_card_details(self):
        suit = self.most_recently_dealt_card.suit
        value = self.most_recently_dealt_card.str_value

        return f'the {value} of {suit}'

class Deck:
    def __init__(self):
        self.cards = []

        for suit in SUITS:
            values_and_scores = zip(STR_VALUES, SCORES)

            for str_value, score in values_and_scores:
                card = Card()
                card.suit = suit
                card.str_value = str_value
                card.score = score

                self.cards.append(card)

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, cards):
        if not isinstance(cards, list):
            raise TypeError("The deck's cards attribute must be a list")

        self._cards = cards

class Participant:

    def __init__(self):
        self.hand = Hand()

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, hand):
        self._hand = hand

    @hand.deleter
    def hand(self):
        del self._hand

    def create_empty_hand(self):
        del self.hand
        self.hand = Hand()

    def is_busted(self):
        return self.hand.score > MAX_WINNING_SCORE

class Player(Participant):
    def __init__(self):
        super().__init__()
        self._bankroll = 5

    @property
    def bankroll(self):
        return self._bankroll

    @bankroll.setter
    def bankroll(self, new_bankroll):
        self._bankroll = new_bankroll

class Dealer(Participant):

    def __init__(self):
        super().__init__()
        self._deck = Deck()

    def recreate_deck(self):
        self._deck = Deck()

    def calculate_number_of_cards_to_deal(self, participant):
        if len(participant.hand.cards) == 0:
            return 2

        return 1

    def update_hand(self, participant, card):
        participant.hand.cards.append(card)
        participant.hand.all_cards_except_last = participant.hand.cards[:-1]
        participant.hand.most_recently_dealt_card = participant.hand.cards[-1]

    def deal(self, participant):
        random.shuffle(self._deck.cards)

        number_of_cards = self.calculate_number_of_cards_to_deal(participant)

        for _ in range(number_of_cards):
            if len(self._deck.cards) == 0:
                self.recreate_deck()

            card = self._deck.cards[0]

            self._deck.cards.remove(card)
            self.update_hand(participant, card)

class GameInterface:
    def prompt(self, message):
        print(f'==> {message}')

    def display_welcome_message(self):
        self.prompt("Welcome to 21! You have $5 in your bankroll. \n")
        time.sleep(0.75)

    def show_cards(self, player, dealer):
        self.prompt(
            f"Your hand contains the \
            {player.hand.get_details_of_all_cards_except_last()} \
            and {player.hand.get_last_dealt_card_details()}.\n"
            )
        time.sleep(0.75)

        self.prompt(
            f"Your hand is worth {player.hand.score} points.\n"
            )
        time.sleep(0.75)

        self.prompt(
            f"One of the dealer's two cards is \
            {dealer.hand.get_last_dealt_card_details()}.\n"
            )
        time.sleep(0.75)

    def get_player_move(self):
        while True:
            self.prompt("Would you like to hit or stay? Enter H for hit " \
            "and S for stay.\n")
            move = input().strip().lower()
            if move in ('h', 's'):
                return move

            self.prompt("That's not a valid choice. Please try again\n.")
            time.sleep(0.75)

    def display_dealing_message(self):
        self.prompt('Dealing additional card...\n')

    def print_updated_player_score(self, player, dealer):
        self.prompt(f'Your new score is {player.hand.score}.\n')
        time.sleep(0.75)

        self.prompt(
            f"As a reminder, one of the dealer's two \
            cards is {dealer.hand.get_last_dealt_card_details()}.\n"
            )
        time.sleep(0.75)

    def print_updated_player_hand(self, player):
        self.prompt(
            f"Your hand now contains the \
            {player.hand.get_details_of_all_cards_except_last()} \
            and {player.hand.get_last_dealt_card_details()}.\n"
            )

    def display_dealer_hand_info(self, required_info, dealer):
        match required_info:
            case 'Dealer hand':
                self.prompt(
                    f"The dealer's hand contains the \
                    {dealer.hand. \
                    get_details_of_all_cards_except_last()} \
                    and {dealer.hand.get_last_dealt_card_details()}.\n"
                    )
            case 'Current score':
                self.prompt(
                    f"The dealer has {dealer.hand.score} points, so \
                    I'm just dealing them another card...\n"
                    )
            case 'Latest card, updated score':
                self.prompt(
                    f"The dealer's new card is \
                    {dealer.hand.get_last_dealt_card_details()}.\n"
                    )

    def display_result(self, result, player, dealer):
        player_score = player.hand.score
        dealer_score = dealer.hand.score
        print(f'Player score: {player_score}')
        print(f'Dealer score: {dealer_score}')

        if result != 'player_bust':
            self.prompt(
                MESSAGES['both_scores'].format \
                (player_score=player_score, dealer_score=dealer_score)
                )
            time.sleep(0.75)

        match result:
            case 'player_bust':
                self.prompt(MESSAGES['new_score'].format \
                (player_score=player_score))
                time.sleep(0.75)

                self.prompt(MESSAGES['player_is_bust'])
                time.sleep(0.75)

            case 'dealer_bust':
                self.prompt(MESSAGES['dealer_is_bust'])
                time.sleep(0.75)

            case 'player_wins':
                self.prompt(MESSAGES['player_is_winner'])
                time.sleep(0.75)

            case 'dealer_wins':
                self.prompt(MESSAGES['player_loses'])
                time.sleep(0.75)

            case 'tie':
                self.prompt(MESSAGES['tie'])
                time.sleep(0.75)

        self.prompt(f'Your bankroll is worth ${player.bankroll}.\n')
        time.sleep(0.75)

    def output_bankroll_status(self, player):
        if player.bankroll == MIN_BANKROLL:
            self.prompt("You've run out of funds. Bummer! \n")

        elif player.bankroll == MAX_BANKROLL:
            self.prompt(
                "You've got $10 in your bankroll! I can't afford to play \
                with you anymore, so I'll have to end the game. \n ")

    def get_player_intention(self, player):
        while True:
            self.prompt("Would you like to play again? Enter Y for yes " \
            "and N for no.\n")
            play_again = input().strip().lower()

            if play_again in ('y', 'n'):
                break

            self.prompt("That's not a valid choice. Please try again\n.")
            time.sleep(0.75)

        return play_again

    def display_continue_message(self):
        self.prompt("Great, let's continue! \n")

    def display_goodbye_message(self):
        self.prompt("Thanks for playing 21! Goodbye!")

class TwentyOneGame:
    DEALER_MINIMUM_SCORE = 17

    games_played = 0

    def __init__(self):
        self._dealer = Dealer()
        self._player = Player()
        self._game_interface = GameInterface()

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        self._player = player

    @property
    def dealer(self):
        return self._dealer

    @dealer.setter
    def dealer(self, dealer):
        self._dealer = dealer

    def start(self):
        self._game_interface.display_welcome_message()

        while True:
            if TwentyOneGame.games_played > 0:
                self.player.create_empty_hand()
                self.dealer.create_empty_hand()

            self.dealer.deal(self.player)
            self.dealer.deal(self.dealer)

            self.player.hand.calculate_value()
            self.dealer.hand.calculate_value()

            self._game_interface.show_cards(self.player, self.dealer)

            self.player_turn()

            if self.player.is_busted():
                result = self.establish_result()
            else:
                self.dealer_turn()
                result = self.establish_result()

            self.update_player_bankroll(result)

            self._game_interface.display_result \
            (result, self.player, self.dealer)

            if self.player.bankroll in (MIN_BANKROLL, MAX_BANKROLL):
                self._game_interface.output_bankroll_status(self.player)
                break

            play_again = self._game_interface.get_player_intention(self.player)

            if play_again == 'y':
                TwentyOneGame.games_played += 1
                os.system('clear')
                self._game_interface.display_continue_message()
                time.sleep(0.75)
            else:
                break

        self._game_interface.display_goodbye_message()

    def player_turn(self):
        while True:
            player_move = self._game_interface.get_player_move()

            if player_move == 'h':
                self.player_hit()

                if self.player.is_busted():
                    break

                self._game_interface.print_updated_player_score \
                (self.player, self.dealer)
            else:
                break

    def player_hit(self):
        os.system('clear')
        self._game_interface.display_dealing_message()
        time.sleep(0.75)
        self.dealer.deal(self.player)
        self._game_interface.print_updated_player_hand(self.player)
        self.player.hand.calculate_value()

    def dealer_turn(self):
        while not self.dealer.is_busted():
            self._game_interface.display_dealer_hand_info \
            ('Dealer hand', self.dealer)

            self.dealer.hand.calculate_value()

            if self.dealer.hand.score >= self.DEALER_MINIMUM_SCORE:
                break

            self._game_interface.display_dealer_hand_info \
            ('Current score', self.dealer)

            self.dealer.deal(self.dealer)
            self.dealer.hand.calculate_value()

            self._game_interface.display_dealer_hand_info \
            ('Latest card, updated score', self.dealer)

            time.sleep(0.75)

    def establish_result(self):
        if self.player.hand.score > MAX_WINNING_SCORE:
            return 'player_bust'

        if self.dealer.hand.score > MAX_WINNING_SCORE:
            return 'dealer_bust'

        if self.player.hand.score > self.dealer.hand.score:
            return 'player_wins'

        if self.dealer.hand.score > self.player.hand.score:
            return 'dealer_wins'

        return 'tie'

    def update_player_bankroll(self, result):
        if result == 'tie':
            pass # Keep the bankroll as it is.
        elif result in ('dealer_bust', 'player_wins'):
            self.player.bankroll += 1
        else:
            self.player.bankroll -= 1

game = TwentyOneGame()
game.start()