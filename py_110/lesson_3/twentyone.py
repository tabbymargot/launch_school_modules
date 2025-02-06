from pprint import pprint
import random

#TODO - move constants into play_21??

VALUES_AS_STRINGS = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

ALL_CARDS = {
    'Clubs': VALUES_AS_STRINGS,
    'Diamonds': VALUES_AS_STRINGS,
    'Hearts': VALUES_AS_STRINGS,
    'Spades': VALUES_AS_STRINGS,
    }

INTEGER_VALUES = {
    'Ace': 1,
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

HIGH_VALUE_ACE = 11

CARDS_IN_HAND = 2

MAX_WINNING_SCORE = 21

def prompt(message):
    print(f'==> {message}')


def initialise_deck():
    deck = []

    for suit, values in ALL_CARDS.items():
        for value in values:
            card = [suit, value]
            deck.append(card)

    # pprint(deck, compact= True)

    return deck

    # deck:
    # [['C', 'A1'], ['C', '2'], ['C', '3'], ['C', '4'], ['C', '5'], ['C', '6'],
    #  ['C', '7'], ['C', '8'], ['C', '9'], ['C', '10'], ['C', 'J'], ['C', 'Q'],
    #  ['C', 'K'], ['C', 'A11'], ['D', 'A1'], ['D', '2'], ['D', '3'], ['D', '4'],
    #  ['D', '5'], ['D', '6'], ['D', '7'], ['D', '8'], ['D', '9'], ['D', '10'],
    #  ['D', 'J'], ['D', 'Q'], ['D', 'K'], ['D', 'A11'], ['H', 'A1'], ['H', '2'],
    #  ['H', '3'], ['H', '4'], ['H', '5'], ['H', '6'], ['H', '7'], ['H', '8'],
    #  ['H', '9'], ['H', '10'], ['H', 'J'], ['H', 'Q'], ['H', 'K'], ['H', 'A11'],
    #  ['S', 'A1'], ['S', '2'], ['S', '3'], ['S', '4'], ['S', '5'], ['S', '6'],
    #  ['S', '7'], ['S', '8'], ['S', '9'], ['S', '10'], ['S', 'J'], ['S', 'Q'],
    #  ['S', 'K'], ['S', 'A11']]


def shuffle(deck):
    return random.shuffle(deck)
    # print(deck)

def deal_cards(deck):
    hand = []
    for _ in range(CARDS_IN_HAND):
        card = random.choice(deck)
        hand.append(card)
        deck.remove(card)

    return hand

def calculate_values(hand_cards, hand_total_worth):
    card_values = []

    for card in hand_cards:
        card_string_value = card[1]
        
        if card_string_value == 'Ace':
            card_value = get_ace_value(hand_total_worth)
        else:
            card_value = INTEGER_VALUES[card_string_value]

        hand_total_worth += card_value
        card_values.append(card_value)

    return card_values, hand_total_worth

def get_ace_value(hand_total_worth):
    if (hand_total_worth + HIGH_VALUE_ACE) <= MAX_WINNING_SCORE:
        return HIGH_VALUE_ACE
    else:
        return INTEGER_VALUES['Ace']
    
def details_of_cards_in_hand(hand):
    all_cards = []

    for card in hand:
        suit = card[0]
        value = card[1]
        all_cards.append(f'the {value} of {suit}')

    all_cards_except_last = all_cards[:-1]
    last_card = all_cards[-1]

    return all_cards_except_last, last_card

        

def play_21():
    deck = initialise_deck()
    player_initial_hand_worth = 0
    dealer_initial_hand_worth = 0

    # Welcome message
    

    # Loop 1 - continue playing
    while True:
    #     shuffle(deck)
    #     pprint(deck, compact= True)

        # Deal all_cards
        # player_hand = deal_cards(deck)
        # dealer_hand = deal_cards(deck)
        # test_hand = [['D', '10'], ['H', 'J']]
        # test_hand2 = [['D', '10'], ['H', 'J'], ['H', 'Ace']]
        player_hand = [['Diamonds', '10'], ['Hearts', 'Jack']]
        dealer_hand = [['Clubs', '8'], ['Spades', 'Queen']]

        # Establish values
        player_card_values, player_updated_hand_worth = calculate_values(player_hand, player_initial_hand_worth)
        # dealer_card_values, dealer_initial_hand_worth = calculate_values(dealer_hand, dealer_initial_hand_worth)



        # print(player_hand, player_card_values, player_initial_hand_worth)
        # print(dealer_hand, dealer_card_values, dealer_initial_hand_worth)

        # values_and_suits_string = details_of_cards_in_hand(player_hand)

        # details_of_cards_in_hand(dealer_hand)

        player_all_cards_except_last, player_last_card = details_of_cards_in_hand(player_hand)
        dealer_all_cards_except_last, dealer_last_card = details_of_cards_in_hand(dealer_hand)

        all_the_players_cards = ', '.join(player_all_cards_except_last) + " and " + player_last_card

        prompt(f"Your hand contains {all_the_players_cards}.\n")
        prompt(f"Your hand is worth {player_updated_hand_worth} points.\n")

        # dealer_all_cards_except_last, dealer_last_card = get_details_of_dealer_cards(dealer_hand)
        prompt(f"One of the dealer's cards is {dealer_last_card}.\n")
            






        # Loop 2 - player turn





            # break - end loop 2

        # If player bust, dealer wins.

        # Loop 3 - dealer turn





            # break - end loop 2

        # If dealer busts, player wins.


        # Compare all_cards and declare winner.

        # Play again?

        break # End loop 1

    # Goodbye message

play_21()