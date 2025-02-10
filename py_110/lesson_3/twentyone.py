import os
import random
import time

VALUES_AS_STRINGS = (['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                    'Jack', 'Queen', 'King'])

ALL_CARDS = {
    'Clubs': VALUES_AS_STRINGS,
    'Diamonds': VALUES_AS_STRINGS,
    'Hearts': VALUES_AS_STRINGS,
    'Spades': VALUES_AS_STRINGS,
    }

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

    return deck

def print_welcome_message():
    prompt("Welcome to 21! \u2665\ufe0f \u2660\ufe0f" \
            "\u2666\ufe0f \u2663\ufe0f \n")
    time.sleep(2)

def print_dealing_and_shuffling():
    prompt("Shuffling cards...\n")
    time.sleep(2)
    prompt("Dealing cards...\n")
    time.sleep(2)

def shuffle(deck):
    random.shuffle(deck)
    return deck

def deal_cards(deck, number_of_cards):
    card_list = []

    for _ in range(number_of_cards):
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
            card_value = calculate_ace_value(hand_score)
        else:
            card_value = INTEGER_VALUES[card_string_value]

        hand_score += card_value

    return hand_score

def print_updated_player_score(player_score, dealer_last_card):
    prompt(f'Your new score is {player_score}.\n')
    time.sleep(1)

    prompt(f"As a reminder, one of the dealer's two " \
            f"cards is {dealer_last_card}.\n")
    time.sleep(1)

def print_updated_dealer_score(dealer_score, dealer_last_card):
    prompt(f"The dealer's new score is {dealer_score}.\n")
    time.sleep(1)

def calculate_ace_value(hand_total_score):
    if (hand_total_score + HIGH_VALUE_ACE) <= MAX_WINNING_SCORE:
        return HIGH_VALUE_ACE

    return LOW_VALUE_ACE

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

def player_turn(player_score, player_hand, deck,
                additional_cards, player_last_card, dealer_last_card):
    while True:
        player_move = get_player_move()
        if player_move == 'h':
            os.system('clear')

            prompt('Dealing additional card...\n')
            time.sleep(1)

            player_hand = get_new_card(deck, additional_cards, player_hand)

            player_all_cards_except_last, player_last_card = \
            details_of_cards_in_hand(player_hand)

            print_updated_player_hand(player_all_cards_except_last, \
            player_last_card)

            player_score = calculate_values(player_hand)

            if player_score > MAX_WINNING_SCORE:
                break

            print_updated_player_score(player_score, dealer_last_card)
        else:
            break

    return player_score

def print_updated_player_hand(player_all_cards_except_last, player_last_card):
    player_cards = ', '.join(player_all_cards_except_last) + \
    " and " + player_last_card

    prompt(f"Your new card is {player_last_card}.\n")
    time.sleep(1)

    prompt(f"Your hand now contains {player_cards}.\n")

def print_updated_dealer_hand(dealer_all_cards_except_last, dealer_last_card):

    prompt(f"The dealer's new card is {dealer_last_card}.\n")
    time.sleep(1)

def get_player_move():
    while True:
        prompt("Would you like to hit or stay? Enter H for hit " \
        "and S for stay.\n")
        move = input().strip().lower()
        if move in ('h', 's'):
            return move

        prompt("That's not a valid choice. Please try again\n.")
        time.sleep(1.5)

def get_new_card(deck, additional_cards, hand):
    new_card = deal_cards(deck, additional_cards)
    hand.append(new_card)

    return hand

def dealer_turn(dealer_score, deck, dealer_hand,
                additional_cards, player_score, dealer_all_cards_except_last, dealer_last_card):
    while dealer_score <= MAX_WINNING_SCORE:
        dealer_cards = ', '.join(dealer_all_cards_except_last) + \
        " and " + dealer_last_card

        prompt(f"The dealer's hand contains {dealer_cards}.\n")

        if dealer_score >= DEALER_MINIMUM_SCORE:
            break

        prompt(f"The dealer has {dealer_score} points, so I'm just " \
        "dealing them another card...\n") 
        time.sleep(1)

        dealer_hand = get_new_card(deck, additional_cards, dealer_hand)

        dealer_all_cards_except_last, dealer_last_card = \
        details_of_cards_in_hand(dealer_hand)

        print_updated_dealer_hand(dealer_all_cards_except_last, \
        dealer_last_card)

        dealer_score = calculate_values(dealer_hand)

    return dealer_score

def establish_result(player_score, dealer_score):
    if player_score > MAX_WINNING_SCORE:
        return 'player_bust'
    if dealer_score > MAX_WINNING_SCORE:
        return 'dealer_bust'
    if player_score > dealer_score:
        return 'player_wins'
    if dealer_score > player_score:
        return 'dealer_wins'

    return 'tie'

def print_result(result, player_score, dealer_score):
    match result:
        case'player_bust':
            prompt(f'Your new score is {player_score}.\n')
            time.sleep(1.5)
            prompt("Oh no - you're bust! \U0001F62D That means the " \
            "dealer's the winner.\n")
            time.sleep(1.5)
        case 'dealer_bust':
            prompt(
            f"You scored {player_score} and the dealer "
            f"scored {dealer_score}.\n "
            )
            time.sleep(1.5)
            prompt("The dealer's bust, so congratulations, you're " \
            "the winner! \U0001F3C6 \n")
            time.sleep(1.5)
        case 'player_wins':
            prompt(
            f"You scored {player_score} and the dealer "
            f"scored {dealer_score}.\n"
            )
            time.sleep(1.5)
            prompt("Congratulations, you're the winner! \U0001F3C6\n")
            time.sleep(1.5)
        case 'dealer_wins':
            prompt(
            f"You scored {player_score} and the dealer "
            f"scored {dealer_score}.\n"
            )
            time.sleep(1.5)
            prompt("Oh no, that means you lost! \U0001F62D \n")
            time.sleep(1.5)
        case 'tie':
            prompt(
            f"You scored {player_score} and the dealer "
            f"scored {dealer_score}. \n"
            )
            time.sleep(1.5)
            prompt("It's a tie! \U0001F454 \n")
            time.sleep(1.5)

def player_wants_to_continue():
    while True:
        prompt("Would you like to continue playing? Enter Y for yes " \
        "and N for no.\n ")
        answer = input().strip().lower()
        if answer in ('y', 'n'):
            return answer

        prompt("That's not a valid choice. Please try again.\n")
        time.sleep(1.5)

def play_21():
    deck = initialise_deck()
    initial_deal = 2
    additional_cards = 1

    print_welcome_message()

    while True:
        print_dealing_and_shuffling()

        deck = shuffle(deck)
        player_hand = deal_cards(deck, initial_deal)
        dealer_hand = deal_cards(deck, initial_deal)
        print(f'DH: {dealer_hand}')
        player_score = calculate_values(player_hand)
        dealer_score = calculate_values(dealer_hand)

        player_all_cards_except_last, player_last_card = (
        details_of_cards_in_hand(player_hand)
        )

        dealer_all_cards_except_last, dealer_last_card = ( details_of_cards_in_hand(dealer_hand)
        )

        all_the_players_cards = ', '.join(player_all_cards_except_last) \
        + " and " + player_last_card

        print_hand_info(all_the_players_cards, player_score, dealer_last_card)

        player_score = player_turn(
        player_score, player_hand, deck, additional_cards, player_last_card, dealer_last_card
        )

        if player_score > MAX_WINNING_SCORE:
            result = establish_result(player_score, dealer_score)
        else:
            dealer_score = dealer_turn(dealer_score, deck, dealer_hand,
                additional_cards, player_score, dealer_all_cards_except_last, dealer_last_card)
            result = establish_result(player_score, dealer_score)

        print_result(result, player_score, dealer_score)

        answer = player_wants_to_continue()

        if answer == 'y':
            prompt("Great, let\'s continue!\n")
            time.sleep(2)
            os.system('clear')
        else:
            prompt("OK then, see you again soon!")
            break

play_21()