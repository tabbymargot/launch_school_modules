""" 
DEAL CARDS
    Problem: Need to deal cards to both the player and the dealer. Will also need to remove those cards from the deck.
    Input - Deck
    Output - List with two sublists (cards)

    Examples:
    [['H', '9']['C', '2']]

    DS:
    Output list

    Algorithm:
        High level - Get 2 random cards (sublists) for the player and 2 for the dealer. Store them in a list and assign each list to a variable. Also remove the cards from the deck.

        Detailed:
        - Initialise empty list player_hand
        - Randomly index into the deck, and retrieve a sublist. 
        - Append this sublist to player_hand.
        - Remove that card from the deck
        - Repeat the above once more.

        - Repeat all steps above to create the dealer_hand



ESTABLISH VALUE OF CARDS AND HANDS

    Problem: 
    Need to establish the integer value of the cards. (Establishing the integer values is necessary at this stage so that the value of any aces can be established and later shown to the player.)

        Rules: 
        The value of any aces will depend on the other cards in the hand

        Input:
        The hand list

        Output:
        New list containing the integer values of the cards.
        Running total of values

        NB: will probably need to reuse this function for additional cards dealt later in the game.

    Algorithm:
        High-level: Get the value of the first card. Get the value of the second card, and if it's an ace calculate its integer value. Add values to hand total and also append values to a list.

        Detailed:
            - Initialise empty list card_values
            - Initialise hand_total to 0
            - Index into the first sublist in hand and get the string at position 1.
            - Get its corresponding integer value from STRINGS_TO_INTEGERS
                - If the card is an ace:
                    - If hand_total + 11 does not exceed 21:
                        Ace = 11
                    - Else:
                        Ace = 1
            - Append that to card_values
            - Add it to hand_total
            - Repeat for the second sublist.

        Return card_values, hand_total

SHOW THE PLAYER THEIR CARDS, AS WELL AS ONE OF THE DEALER'S CARDS
    Problem: Output a string with the suits and values of the cards, and the value of the hand, interpolated into the string. Do the same to display one of the dealer's cards.

    Input:
    Sublists containing the cards' suits and values
    hand_value (integer)

    Output:
    f-string

    DS
    Nested list?
    String?

    Algorithm:
        High-level: For the cards' suits and values, for each card concatenate into a string, eg '2 of Hearts'. Then concatenate into a longer_string containing all the cards, eg '2 of Hearts, 3 of Clubs and Jack of Spades'. Interpolate this string into a longer string, eg "Your hand contains the '2 of Hearts, 3 of Clubs and Jack of Spades'. Get the hand_value and use string interpolation to show the player how much their hand is worth.

        card_list = []

        For card in cards:
            - Initialise empty card_string
            - Concatenate the + value + of + suit together and assign to card_string
                - If it's the last card in the hand, will need to add the word 'and' before 'the'.
            - Append card_string to card_list
            - Join all the card strings using a comma as a delimiter, creating a string with all the cards. Assign to longer_string.


        Output a longer f-string:
        "Your hand contains the following cards: {longer_string}. Your hand is worth {hand_value} points"






Things to think about:
- What happens if the deck runs out of cards?
- Add emojis to suits?

    
    
    
    
    
    
    
    
    
    
    
    
"""