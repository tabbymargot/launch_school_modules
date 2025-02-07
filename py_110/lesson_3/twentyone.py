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

# INITIAL_DEAL = 2

# ADDITIONAL_CARDS = 1

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

#TODO - add code to clear terminal display
def shuffle(deck):
    random.shuffle(deck)
    return deck

def deal_cards(deck, number_of_cards):
    card_list = []
    #TODO cards should be from top of deck!!!
    for _ in range(number_of_cards):
        # card = random.choice(deck)
        card = deck[0]
        card_list.append(card)
        deck.remove(card)

    if len(card_list) == 1:
        return card_list[0]

    return card_list

def calculate_values(hand_cards):
    hand_score = 0

    for card in hand_cards:
        card_string_value = card[1]
        
        if card_string_value == 'Ace':
            card_value = get_ace_value(hand_score)
        else:
            card_value = INTEGER_VALUES[card_string_value]

        hand_score += card_value

    return hand_score

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



def print_hand_info(all_the_players_cards, player_score, dealer_last_card):
    prompt(f"Your hand contains {all_the_players_cards}.\n")
    time.sleep(1)

    prompt(f"Your hand is worth {player_score} points.\n")
    time.sleep(1)

    prompt(f"One of the dealer's two cards is {dealer_last_card}.\n")
    time.sleep(1)

def player_turn(player_score, player_hand, deck, additional_cards):
    while True:
        player_move = get_player_move()
        if player_move == 'h':
            new_card = deal_cards(deck, additional_cards)
            player_hand.append(new_card)

            player_all_cards_except_last, player_last_card = details_of_cards_in_hand(player_hand)

            print_updated_player_hand(player_all_cards_except_last, player_last_card)

            player_score = calculate_values(player_hand)

            if player_score > MAX_WINNING_SCORE:
                # print_busted_message(player_score)
                break

            prompt(f'Your new score is {player_score}.\n')
            time.sleep(1)
        else:
            break

    return player_score
            # break # end loop 2 - player turn

def print_updated_player_hand(player_all_cards_except_last, player_last_card):
    player_cards = ', '.join(player_all_cards_except_last) + " and " + player_last_card

    prompt(f"Your new card is {player_last_card}.\n")
    time.sleep(1)

    prompt(f"Your hand now contains {player_cards}.\n")


def get_player_move():
    while True:
        prompt('Would you like to hit or stay? Enter H for hit and S for stay.\n')
        move = input().strip().lower()
        if move in ('h', 's'):
            return move

        prompt("That's not a valid choice. Please try again\n.")
        time.sleep(1.5)

def print_busted_message(player_score):
    prompt(f'Your new score is {player_score}.\n')
    time.sleep(1)
    prompt(f"Oh no - you've busted! That means the dealer's the winner.\n")

def dealer_turn(dealer_score, dealer_hand, deck, additional_cards):
    while dealer_score <= MAX_WINNING_SCORE:

            if dealer_score < DEALER_MINIMUM_SCORE:
                prompt(f'The dealer has {dealer_score} points, so I\'m just dealing them another card...\n')
                time.sleep(2)
                dealer_hand.append(deal_cards(deck, additional_cards))
                dealer_score = calculate_values(dealer_hand)
                print(f'LOOP dealer score: {dealer_score}')
                
            else:
                break
    return dealer_score

def establish_result(player_score, dealer_score):
    if player_score > MAX_WINNING_SCORE:
        return 'player_busted'
    elif dealer_score > MAX_WINNING_SCORE:
        return 'dealer_busted'
    elif player_score > dealer_score:
        return 'player_wins'
    elif dealer_score > player_score:
        return 'dealer_wins'
    else:
        return 'tie'
    
def print_result(result, player_score, dealer_score):
    match result:
        case'player_busted':
            prompt(f'Your new score is {player_score}.\n')
            time.sleep(1)
            prompt(f"Oh no - you've busted! That means the dealer's the winner.\n")
            time.sleep(1)
        case 'dealer_busted':
            prompt(f'You scored {player_score} and the dealer scored {dealer_score}.\n')
            time.sleep(1.5)
            prompt("The dealer busted, so congratulations, you're the winner!\n")
            time.sleep(1.5)
        case 'player_wins':
            prompt(f'You scored {player_score} and the dealer scored {dealer_score}.\n')
            time.sleep(1.5)
            prompt("Congratulations, you're the winner!\n")
            time.sleep(1.5)
        case 'dealer_wins':
            prompt(f'You scored {player_score} and the dealer scored {dealer_score}.\n')
            time.sleep(1.5)
            prompt("Oh no, that means you lost!\n")
            time.sleep(1.5)
        case 'tie':
            prompt(f'You scored {player_score} and the dealer scored {dealer_score}.\n')
            time.sleep(1.5)
            prompt("It's a tie! (Could be worse.)\n")
            time.sleep(1.5)

def player_wants_to_continue():
    while True:
        prompt('Would you like to continue playing? Enter Y for yes and N for no.\n')
        answer = input().strip().lower()
        if answer in ('y', 'n'):
            return answer

        prompt("That's not a valid choice. Please try again.\n")
        time.sleep(1.5)

def play_21():
    deck = initialise_deck()
    initial_deal = 2
    additional_cards = 1

    #TODO WELCOME MESSAGE
    
    while True:
        deck = shuffle(deck)
        player_hand = deal_cards(deck, initial_deal)
        dealer_hand = deal_cards(deck, initial_deal)
        player_score = calculate_values(player_hand)
        dealer_score = calculate_values(dealer_hand)

        print(f'TOG dealer score: {dealer_score}')

        player_all_cards_except_last, player_last_card = details_of_cards_in_hand(player_hand)
        dealer_all_cards_except_last, dealer_last_card = details_of_cards_in_hand(dealer_hand)

        all_the_players_cards =  ', '.join(player_all_cards_except_last) + " and " + player_last_card

        print_hand_info(all_the_players_cards, player_score, dealer_last_card)

        player_score = player_turn(player_score, player_hand, deck, additional_cards)
        
        #TODO - need to move this into the messages function. At the moment the game stops after this message prints.
        if player_score > MAX_WINNING_SCORE:
            result = establish_result(player_score, dealer_score)
        else:
            dealer_score = dealer_turn(dealer_score, dealer_hand, deck, additional_cards)

            result = establish_result(player_score, dealer_score)

        print_result(result, player_score, dealer_score)

        answer = player_wants_to_continue()

        if answer == 'y':
            prompt("Great, let\'s continue!\n")
            time.sleep(1.5)
        else:
            prompt("OK then, see you again soon!")
            break

play_21()