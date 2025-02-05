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

def card_and_hand_values(hand, hand_total_value):
    card_values = []

    for card in hand:
        card_string_value = card[1]
        
        if card_string_value == 'Ace':
            card_value = get_ace_value(hand_total_value)
        else:
            card_value = INTEGER_VALUES[card_string_value]

        hand_total_value += card_value
        card_values.append(card_value)

    return card_values, hand_total_value

def get_ace_value(hand_total_value):
    if (hand_total_value + HIGH_VALUE_ACE) <= 21:
        return HIGH_VALUE_ACE
    else:
        return INTEGER_VALUES['Ace']
    
def details_of_cards_in_hand(hand):
    all_cards_except_last = []

    for card in hand:
        suit = card[0]
        value = card[1]
        value_of_suit_string = f'the {value} of {suit}'

        if card != hand[-1]:
            all_cards_except_last.append(value_of_suit_string)

    return ', '.join(all_cards_except_last) + " and " + value_of_suit_string
        
    


def play_21():
    deck = initialise_deck()
    player_hand_total_value = 0
    dealer_hand_total_value = 0

    # Welcome message
    

    # Loop 1 - continue playing
    while True:
    #     shuffle(deck)
    #     pprint(deck, compact= True)

        # Deal cards
        player_hand = [['Diamonds', '10'], ['Hearts', 'Jack'], ['Hearts', 'Ace']]
        # dealer_hand = deal_cards(deck)
        # test_hand = [['D', 'Ace'], ['H', 'Ace']]
        # test_hand2 = [['D', '10'], ['H', 'J'], ['H', 'Ace']]

        # Establish values
        player_card_values, player_hand_total_value = card_and_hand_values(player_hand, player_hand_total_value)
        # dealer_card_values, dealer_hand_total_value = card_and_hand_values(dealer_hand, dealer_hand_total_value)



        # print(player_hand, player_card_values, player_hand_total_value)
        # print(dealer_hand, dealer_card_values, dealer_hand_total_value)

        values_and_suits_string = details_of_cards_in_hand(player_hand)

        prompt(f"Your hand contains {values_and_suits_string}.\n")
        prompt(f"Your hand is worth {player_hand_total_value} points.\n")
            






        # Loop 2 - player turn





            # break - end loop 2

        # If player bust, dealer wins.

        # Loop 3 - dealer turn





            # break - end loop 2

        # If dealer busts, player wins.


        # Compare cards and declare winner.

        # Play again?

        break # End loop 1

    # Goodbye message

play_21()