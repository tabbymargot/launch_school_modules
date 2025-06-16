# TODO: make the deck a collaborator object of Dealer rather than passing it in as an argument to the various methods?
import os
import random

class Card:
    # VALUES_AS_STRINGS = (['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'])

    # ALL_CARDS = {
    #     'Clubs': VALUES_AS_STRINGS,
    #     'Diamonds': VALUES_AS_STRINGS,
    #     'Hearts': VALUES_AS_STRINGS,
    #     'Spades': VALUES_AS_STRINGS,
    #     }
    def __init__(self, suit, str_value):
        self.suit = suit
        self.str_value = str_value
        # self.score = score

class Hand():
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

    LOW_VALUE_ACE = 1
    HIGH_VALUE_ACE = 11
    #TODO: there are now 2 constants with the same name
    MAX_WINNING_SCORE = 21

    most_recently_dealt_card = None

    def __init__(self):
        self.cards = []
        self.score = None

    def calculate_value(self):
        aces = []
        non_aces = []

        for card in self.cards:
            if list(card)[1] == 'Ace':
                aces.append(card)
            else:
                non_aces.append(card)

        non_aces_values = [self.INTEGER_VALUES[card[1]] for card in non_aces]
        non_aces_score = sum(non_aces_values)

        aces_score = self.calculate_ace_values(aces, non_aces_score)
        # print(non_aces_score)
        # print(aces_score)

        self.score = non_aces_score + aces_score
        # print(non_aces_score + aces_score)
    
    def calculate_ace_values(self, aces, non_aces_score):
        aces_values = []

        for _ in aces:
            if ((non_aces_score + sum(aces_values) + self.HIGH_VALUE_ACE)
            <= self.MAX_WINNING_SCORE):
                aces_values.append(self.HIGH_VALUE_ACE)

            elif ((non_aces_score + sum(aces_values) + self.LOW_VALUE_ACE)
            <= self.MAX_WINNING_SCORE):
                aces_values.append(self.LOW_VALUE_ACE)

            elif self.HIGH_VALUE_ACE in aces_values:
                for idx, value in enumerate(aces_values):
                    if value == self.HIGH_VALUE_ACE:
                        aces_values[idx] = self.LOW_VALUE_ACE
                        break

                aces_values.append(self.LOW_VALUE_ACE)

            else:
                pass

        return sum(aces_values)
    
    def card_details(self):
        all_cards = []

        for card in self.cards:
            suit = card[0]
            value = card[1]
            all_cards.append(f'the {value} of {suit}')

        all_player_cards_except_last = all_cards[:-1]
        player_last_card = all_cards[-1]

        return all_player_cards_except_last, player_last_card

class Deck:
    SCORES = {
        'Ace': (1, 11),
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
     
    VALUES_AS_STRINGS = (['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'])

    ALL_CARDS = {
        'Clubs': VALUES_AS_STRINGS,
        'Diamonds': VALUES_AS_STRINGS,
        'Hearts': VALUES_AS_STRINGS,
        'Spades': VALUES_AS_STRINGS,
        }

    def __init__(self):
        self.cards = []

        # Initialise the deck's cards with their suits and values
        for suit, values in self.ALL_CARDS.items():
            for value in values:
                cards = Card(suit, value)
                self.cards.append(cards)

        # Then add a score attribute to each card
        # TODO: refactor using properties
        for card in self.cards:
            card.score = self.SCORES[card.str_value]
            print(vars(card)) 

        # print(vars(self.cards[0]))  
        print(len(self.cards))

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

        if len(participant.hand.cards) == 0:
            number_of_cards_to_deal = 2
        else:
            number_of_cards_to_deal = 1

        # print(f'First: {participant.hand.cards}')
        
        for _ in range(number_of_cards_to_deal):
            card = deck.cards[0]
            participant.hand.cards.append(card)
            deck.cards.remove(card)
            print(card in deck.cards)

        # print(f'Second: {participant.hand.cards}') 

        if len(participant.hand.cards) == 1:
            return participant.hand.cards[0]

        return participant.hand
    
    # player_hand = Dealer.deal_new_card(self, self.deck, self.player)
    def deal_new_card(self, deck, participant):
        updated_hand = Dealer.deal(self, deck, participant)
        # print(f'NC: {updated_hand.cards}')
        # participant.hand.cards.append(new_card)

        return participant.hand
            
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
        # print(self.player.hand.cards)

        self.deal_cards(self.dealer)
        # print(self.dealer.hand.cards)

        self.player.hand.calculate_value()
        self.dealer.hand.calculate_value()

        # print (self.player.hand.score)
        # print (self.dealer.hand.score)

        self.show_cards()

        player_score = self.player_turn()
        print(f'Player score: {player_score}')

        if player_score > self.MAX_WINNING_SCORE:
            result = self.establish_result()
        else:
            dealer_score = self.dealer_turn()
            print(f'The dealers final score 1: {dealer_score}')
            result = self.establish_result()

        # result = self.establish_result(player_score, dealer_score)
        print(f'This is the result: {result}')

        # self.dealer_turn()
            # The dealer doesn't play at all if the player busts.
            # Display the dealer's hand, sincluding the hidden card, and report his point total.
            # Redisplay the dealer's hand and point total and each time he hits.
            # Display the results when the dealer stays.

        self.display_result(result)

        # TODO: After each game is over, ask the player if they want to play again. Start a new game if they say yes, else end the game.

        self.display_goodbye_message()

    def deal_cards(self, participant):
        self.dealer.deal(self.deck, participant)

    def show_cards(self):
        all_player_cards_except_last, player_last_card = self.player.hand.card_details()

        #TODO: only the second variable is used.
        all_dealer_cards_except_last, dealer_last_card = self.dealer.hand.card_details()

        all_the_players_cards = ', '.join(all_player_cards_except_last) \
        + " and " + player_last_card

        # all_the_dealers_cards = ', '.join(all_dealer_cards_except_last) \
        # + " and " + dealer_last_card

        self.prompt(f"Your hand contains {all_the_players_cards}.\n")
        # time.sleep(1)

        self.prompt(f"Your hand is worth {self.player.hand.score} points.\n")
        # time.sleep(1)

        self.prompt(f"One of the dealer's two cards is {dealer_last_card}.\n")
        # time.sleep(1)

    def player_turn(self):
        while True:
            player_move = self.get_player_move()
            # print(player_move)
            # break
            if player_move == 'h':
                os.system('clear')

                self.prompt('Dealing additional card...\n')
                # time.sleep(1)

                player_hand = Dealer.deal_new_card(self, self.deck, self.player)
                print(f'PHC: {player_hand.cards}')

                # player_all_cards_except_last, player_last_card = \
                # print(self.player.hand.card_details())

                all_player_cards_except_last, player_last_card = self.player.hand.card_details()

                self.print_updated_player_hand(all_player_cards_except_last, \
                player_last_card)

                self.player.hand.calculate_value()

                player_score = self.player.hand.score

                if player_score > self.MAX_WINNING_SCORE:
                    break

                self.print_updated_player_score()
            else:
                break

        return self.player.hand.score

    def get_player_move(self):
        while True:
            self.prompt("Would you like to hit or stay? Enter H for hit " \
            "and S for stay.\n")
            move = input().strip().lower()
            if move in ('h', 's'):
                return move

            self.prompt("That's not a valid choice. Please try again\n.")
            # time.sleep(1.5)

    def print_updated_player_hand(self, player_all_cards_except_last, player_last_card):
        player_cards = ', '.join(player_all_cards_except_last) + \
        " and " + player_last_card

        self.prompt(f"Your new card is {player_last_card}.\n")
        # time.sleep(1)

        self.prompt(f"Your hand now contains {player_cards}.\n")

    def print_updated_player_score(self):
        self.prompt(f'Your new score is {self.player.hand.score}.\n')
        # time.sleep(1)

        #TODO: only the second variable is used.
        all_dealer_cards_except_last, dealer_last_card = self.dealer.hand.card_details()

        self.prompt(f"As a reminder, one of the dealer's two " \
                f"cards is {dealer_last_card}.\n")
        # # time.sleep(1)

    
    def dealer_turn(self):
        print(f'Dealer score: {self.dealer.hand.score}')
        while self.dealer.hand.score <= self.MAX_WINNING_SCORE:

            #TODO: Find a better way to get the values below
            all_dealer_cards_except_last, dealer_last_card = self.dealer.hand.card_details()

            dealer_cards = ', '.join(all_dealer_cards_except_last) + \
            " and " + dealer_last_card

            self.prompt(f"The dealer's hand contains {dealer_cards}.\n")

            # print(f'Dealers original score: {self.dealer.hand.score}')

            self.dealer.hand.calculate_value()

            if self.dealer.hand.score >= self.DEALER_MINIMUM_SCORE:
                break

            self.prompt(f"The dealer has {self.dealer.hand.score} points, so I'm just " \
            "dealing them another card...\n") 
            # time.sleep(1)

            

            dealer_hand = self.dealer.deal_new_card(self.deck, self.dealer)
            # print(f'Dealer hand: {dealer_hand.cards}')
             

            all_dealer_cards_except_last, dealer_last_card = self.dealer.hand.card_details()

            # self.dealer.hand.calculate_value()

            # dealer_score = self.dealer.hand.score

            # self.prompt(f"The dealer's new card is {dealer_last_card}, and their new score is {dealer_score}.\n")
            # time.sleep(1)
        print(f'The dealers final score 2: {self.dealer.hand.score}')
        #TODO: I shouldn't have to return this
        return self.dealer.hand.score

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