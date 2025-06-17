# TODO: make the deck a collaborator object of Dealer rather than passing it in as an argument to the various methods?

# TODO: check no methods return a value and also have side effects
import os
import random

class Card:
    def __init__(self, suit, str_value, score):
        self.suit = suit
        self.str_value = str_value
        self.score = score

        # TODO: create getters and setters?


class Hand():
    #TODO: there are now 2 constants with the same name
    MAX_WINNING_SCORE = 21

    most_recently_dealt_card = None

    def __init__(self):
        self.cards = []
        self.score = None
        self.all_cards_except_last = None
        self.most_recently_dealt_card = None

    def calculate_value(self):
        aces = []
        non_aces = []

        for card in self.cards:
            if card.str_value == 'Ace':
                aces.append(card)
            else:
                non_aces.append(card)

        non_aces_values = [card.score for card in non_aces]
        non_aces_score = sum(non_aces_values)

        aces_score = self.calculate_ace_values(aces, non_aces_score)
        # print(non_aces_score)
        # print(aces_score)

        self.score = non_aces_score + aces_score
        # print(f'This is the score: {self.score}')
        # print(non_aces_score + aces_score)
    
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
    
    def get_card_details(self):
        card_details = []

        for card in self.all_cards_except_last:
            suit = card.suit
            value = card.str_value
            card_details.append(f'the {value} of {suit}')

        return card_details

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
                self.cards.append(Card(suit, str_value, score))
            
            # for card in self.cards:
            #     print(vars(card))

            # print(len(self.cards))

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

    def __init__(self):
        super().__init__()

    def deal(self, deck, participant):
        random.shuffle(deck.cards)

        # for card in deck.cards:
        #     print(vars(card))

        if len(participant.hand.cards) == 0:
            number_of_cards_to_deal = 2
        else:
            number_of_cards_to_deal = 1
        
        for _ in range(number_of_cards_to_deal):
            card = deck.cards[0]

            participant.hand.cards.append(card)
            deck.cards.remove(card)

            participant.hand.all_cards_except_last = participant.hand.cards[:-1]
            participant.hand.most_recently_dealt_card = participant.hand.cards[-1]
            
    def hide(self):
        # STUB
        pass

    def reveal(self):
        # STUB
        pass

class TwentyOneGame:
    MAX_WINNING_SCORE = 21
    DEALER_MINIMUM_SCORE = 17

    def __init__(self):
        # STUB
        # What attributes does the game need? A deck? Two
        #   participants?
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()

    def prompt(self, message):
        print(f'==> {message}')

    def display_welcome_message(self):
        self.prompt("Welcome to 21!")

    def start(self):
        # SPIKE
        self.display_welcome_message()

        # TODO: When the program starts, give the player 5 dollars with which to bet. Deduct 1 dollar each time she loses, and add 1 dollar each time she wins. The program should quit when she is broke (0 dollars) or rich (has a total of 10 dollars).

        # TODO: WHILE player wants to continue
        # TODO: Be prepared to run out of cards. You can either create a new deck for each game, or keep track of how many cards remain and create a new deck as needed.

        self.deal_cards(self.player)
        self.deal_cards(self.dealer)

        self.player.hand.calculate_value()
        self.dealer.hand.calculate_value()

        self.show_cards()

        # player_score = self.player_turn()
        self.player_turn()
        # print(f'Player score: {player_score}')

        if self.player.hand.score > self.MAX_WINNING_SCORE:
            result = self.establish_result()
        else:
            # dealer_score = self.dealer_turn()
            # print(f'The dealers final score 1: {dealer_score}')
            self.dealer_turn()
            result = self.establish_result()

        # result = self.establish_result(player_score, dealer_score)
        # print(f'This is the result: {result}')

        self.display_result(result)

        # TODO: After each game is over, ask the player if they want to play again. Start a new game if they say yes, else end the game.

        self.display_goodbye_message()

    def deal_cards(self, participant):
        self.dealer.deal(self.deck, participant)

    def show_cards(self):
        self.prompt(f"Your hand contains the {self.player.hand.get_card_details()} and {self.player.hand.get_last_dealt_card_details()}.\n")
        # time.sleep(1)

        self.prompt(f"Your hand is worth {self.player.hand.score} points.\n")
        # time.sleep(1)

        self.prompt(f"One of the dealer's two cards is {self.dealer.hand.get_last_dealt_card_details()}.\n")
        # time.sleep(1)

    def player_turn(self):
        while True:
            player_move = self.get_player_move()
            # print(player_move)
            # break
            # TODO: Move hit / stay to Participant class?
            if player_move == 'h':
                os.system('clear')

                self.prompt('Dealing additional card...\n')
                # time.sleep(1)

                self.dealer.deal(self.deck, self.player)

                self.print_updated_player_hand()

                self.player.hand.calculate_value()

                # player_score = self.player.hand.score

                if self.player.hand.score > self.MAX_WINNING_SCORE:
                    break

                self.print_updated_player_score()
            else:
                break

        # return self.player.hand.score

    def get_player_move(self):
        while True:
            self.prompt("Would you like to hit or stay? Enter H for hit " \
            "and S for stay.\n")
            move = input().strip().lower()
            if move in ('h', 's'):
                return move

            self.prompt("That's not a valid choice. Please try again\n.")
            # time.sleep(1.5)

    def print_updated_player_hand(self):

        self.prompt(f"Your hand now contains the {self.player.hand.get_card_details()} and {self.player.hand.get_last_dealt_card_details()}.\n")

    def print_updated_player_score(self):
        self.prompt(f'Your new score is {self.player.hand.score}.\n')
        # time.sleep(1)

        self.prompt(f"As a reminder, one of the dealer's two " \
                f"cards is {self.dealer.hand.get_last_dealt_card_details()}.\n")
        # # time.sleep(1)

    
    def dealer_turn(self):
        while self.dealer.hand.score <= self.MAX_WINNING_SCORE:

            self.prompt(f"The dealer's hand contains the {self.dealer.hand.get_card_details()} and {self.dealer.hand.get_last_dealt_card_details()}.\n")

            self.dealer.hand.calculate_value()

            if self.dealer.hand.score >= self.DEALER_MINIMUM_SCORE:
                break

            self.prompt(f"The dealer has {self.dealer.hand.score} points, so I'm just " \
            "dealing them another card...\n") 
            # time.sleep(1)

            self.dealer.deal(self.deck, self.dealer)

            self.dealer.hand.calculate_value()
            
            self.prompt(f"The dealer's new card is {self.dealer.hand.get_last_dealt_card_details()}, and their new score is {self.dealer.hand.score}.\n")
            # time.sleep(1)
        # print(f'The dealers final score 2: {self.dealer.hand.score}')
        #TODO: I shouldn't have to return this
        # return self.dealer.hand.score

    def display_goodbye_message(self):
        print("Thanks for playing 21! Goodbye!")

    def establish_result(self):
        # Is it necessary to define variables here?
        player_score = self.player.hand.score
        dealer_score = self.dealer.hand.score

        if player_score > self.MAX_WINNING_SCORE:
            return 'player_bust'
        if dealer_score > self.MAX_WINNING_SCORE:
            return 'dealer_bust'
        if player_score > dealer_score:
            return 'player_wins'
        if dealer_score > player_score:
            return 'dealer_wins'

        return 'tie'

    def display_result(self, result):
        player_score = self.player.hand.score
        dealer_score = self.dealer.hand.score

        match result:
            case 'player_bust':
                self.prompt(f'Your new score is {player_score}.\n')
                # time.sleep(1.5)
                self.prompt("Oh no - you're bust! \U0001F62D That means the " \
                "dealer's the winner.\n")
                # time.sleep(1.5)
            case 'dealer_bust':
                self.prompt(
                f"You scored {player_score} and the dealer "
                f"scored {dealer_score}.\n "
                )
                # time.sleep(1.5)
                self.prompt("The dealer's bust, so congratulations, you're " \
                "the winner! \U0001F3C6 \n")
                # time.sleep(1.5)
            case 'player_wins':
                self.prompt(
                f"You scored {player_score} and the dealer "
                f"scored {dealer_score}.\n"
                )
                # time.sleep(1.5)
                self.prompt("Congratulations, you're the winner! \U0001F3C6\n")
                # time.sleep(1.5)
            case 'dealer_wins':
                self.prompt(
                f"You scored {player_score} and the dealer "
                f"scored {dealer_score}.\n"
                )
                # time.sleep(1.5)
                self.prompt("Oh no, that means you lost! \U0001F62D \n")
                # time.sleep(1.5)
            case 'tie':
                self.prompt(
                f"You scored {player_score} and the dealer "
                f"scored {dealer_score}. \n"
                )
                # time.sleep(1.5)
                self.prompt("It's a tie! \U0001F454 \n")
                # time.sleep(1.5)

game = TwentyOneGame()
game.start()