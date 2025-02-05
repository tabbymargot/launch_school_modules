from pprint import pprint
import random

STRING_CARD_VALUES = [['A1', 'A11'], '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

DIGIT_CARD_VALUES = {
    'A1': 1,
    '2': 1,
    '3': 1,
    '4': 1,
    '4': 1,
    '6': 1,
    '7': 1,
    '8': 1,
    '9': 1,
    '10': 1,
    'J': 1,
    'Q': 1,
    'K': 1,
    'A11': 11,
}

DECK = {
    'C': STRING_CARD_VALUES,
    'D': STRING_CARD_VALUES,
    'H': STRING_CARD_VALUES,
    'S': STRING_CARD_VALUES,
    }


def initialise_deck():
    deck = []

    for suit, values in DECK.items():
        for value in values:
            card = [suit, value]
            deck.append(card)

    pprint(deck, compact= True)

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

def play_21():
    deck = initialise_deck()

    # Welcome message
    

    # Loop 1 - continue playing
    # while True:
    #     shuffle(deck)
    #     pprint(deck, compact= True)

        # Deal cards

        # Loop 2 - player turn





            # break - end loop 2

        # If player bust, dealer wins.

        # Loop 3 - dealer turn





            # break - end loop 2

        # If dealer busts, player wins.


        # Compare cards and declare winner.

        # Play again?

        # break # End loop 1

    # Goodbye message

play_21()