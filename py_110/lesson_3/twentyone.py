from pprint import pprint
import random

#TODO - move constants into play_21??
VALUES_AS_STRINGS = [['A1', 'A11'], '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

STRINGS_TO_INTEGERS = {
    'A1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '4': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
    'A11': 11,
}

ALL_CARDS = {
    'C': VALUES_AS_STRINGS,
    'D': VALUES_AS_STRINGS,
    'H': VALUES_AS_STRINGS,
    'S': VALUES_AS_STRINGS,
    }

# INITIAL_DEAL = 4
CARDS_IN_HAND = 2


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


def play_21():
    deck = initialise_deck()

    # Welcome message
    

    # Loop 1 - continue playing
    while True:
    #     shuffle(deck)
    #     pprint(deck, compact= True)

        # Deal cards
        player_hand = deal_cards(deck)
        dealer_hand = deal_cards(deck)

        # player_hand = []

        # for _ in range(CARDS_IN_HAND):
        #     player_hand.append(random.choice(deck))
        
        # print(player_hand)

        # dealer_hand = []
        # for _ in range(CARDS_IN_HAND):
        #     dealer_hand.append(random.choice(deck))
        
        # print(dealer_hand)


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