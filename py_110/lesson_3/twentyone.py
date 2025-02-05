from pprint import pprint
import random
import time

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

INITIAL_CARDS_IN_HAND = 2

MAX_WINNING_SCORE = 21

DEALER_MINIMUM_SCORE = 17

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

def deal_cards(deck, number_of_cards):
    card_list = []
    for _ in range(number_of_cards):
        card = random.choice(deck)
        card_list.append(card)
        deck.remove(card)

    if len(card_list) == 1:
        return card_list[0]

    return card_list

def calculate_values(hand_cards):
    card_values = []
    hand_score = 0

    for card in hand_cards:
        card_string_value = card[1]
        
        if card_string_value == 'Ace':
            card_value = get_ace_value(hand_score)
        else:
            card_value = INTEGER_VALUES[card_string_value]

        hand_score += card_value
        card_values.append(card_value)

    # TODO - remove card_values if it's not being used anywhere
    return card_values, hand_score

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


def get_player_card_string(player_hand):
    player_all_cards_except_last, player_last_card = details_of_cards_in_hand(player_hand)

    return ', '.join(player_all_cards_except_last) + " and " + player_last_card


def get_player_move():
    while True:
        prompt('Would you like to hit or stay? Enter H for hit and S for stay.\n')
        move = input().strip().lower()
        if move in ('h', 's'):
            return move

        prompt("That's not a valid choice. Please try again\n.")
        time.sleep(1.5)


        

def play_21():
    deck = initialise_deck()
    player_starting_score = 0
    dealer_starting_score = 0
    initial_deal = 2
    additional_cards = 1

    # WELCOME MESSAGE
    

    # LOOP 1 - CONTINUE PLAYING
    while True:
    #     shuffle(deck)
    #     pprint(deck, compact= True)

        # DEAL ALL CARDS
        player_hand = deal_cards(deck, initial_deal)
        dealer_hand = deal_cards(deck, initial_deal)
        # test_hand = [['D', '10'], ['H', 'J']]
        # test_hand2 = [['D', '10'], ['H', 'J'], ['H', 'Ace']]
        # player_hand = [['Diamonds', '2'], ['Hearts', '3']]
        # dealer_hand = [['Clubs', '8'], ['Spades', 'Queen']]

        # CALCULATE CARD AND HAND VALUES
        player_cards_numeric_values, player_score = calculate_values(player_hand)
        dealer_cards_numeric_values, dealer_score = calculate_values(dealer_hand)
        print(f'TOG dealer score: {dealer_score}')

        player_all_cards_except_last, player_last_card = details_of_cards_in_hand(player_hand)
        dealer_all_cards_except_last, dealer_last_card = details_of_cards_in_hand(dealer_hand)

        # all_the_players_cards = all_the_cards(player_all_cards_except_last, player_last_card)

        all_the_players_cards =  ', '.join(player_all_cards_except_last) + " and " + player_last_card

        prompt(f"Your hand contains {all_the_players_cards}.\n")
        prompt(f"Your hand is worth {player_score} points.\n")
        prompt(f"One of the dealer's card_list is {dealer_last_card}.\n")

        # LOOP 2 - PLAYER TURN
        while True:
            player_move = get_player_move()
            if player_move == 'h':
                player_hand.append(deal_cards(deck, additional_cards))

                prompt(f"Your hand now contains {get_player_card_string(player_hand)}.\n")

                player_cards_numeric_values, player_score = calculate_values(player_hand)

                if player_score > MAX_WINNING_SCORE:
                    prompt(f"That was a bad choice: your score is now {player_score} and you've busted!\n")
                    break

                prompt(f'Your new score is {player_score}')
            else:
                break # end loop 2 - player turn
        
        # LOOP 3 - DEALER TURN
        while True:
            # Break if dealer score higher than player score
            # Move this to hit or stay function? Do same with player turn?
            
            print(f'LOOP dealer score: {dealer_score}')

            if dealer_score < DEALER_MINIMUM_SCORE:
                dealer_hand.append(deal_cards(deck, additional_cards))

            elif dealer_score <= MAX_WINNING_SCORE:
                if dealer_score < player_score:
                    dealer_hand.append(deal_cards(deck, additional_cards))
            
            elif dealer_score > MAX_WINNING_SCORE:
                prompt('Dealer busts!')
                break

            # Move the rest to a calculate winner function

            if dealer_score == player_score:
                # prompt("It's a tie!")
                break
                # store final dealer score

            if dealer_score > player_score:
                # prompt('Dealer wins!')
                break
                # store final dealer score

            dealer_cards_numeric_values, dealer_score = calculate_values(dealer_hand)

            
        



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