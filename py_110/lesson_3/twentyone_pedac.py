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



ESTABLISH VALUE OF CARDS 

    Problem: 
    Need to establish the integer value of the cards. (Establishing the integer values is necessary so that the value of any aces can be established.)

        Rules: 
        The value of any aces will depend on the other cards in the hand

        Input:
        player_hand and dealer_hand lists

        Output:
        New lists containing the integer values of the cards (one for each player)

        NB: will probably need to reuse this function for additional cards dealt later in the game.

    Algorithm:
        High-level: Get the value of the first card. Get the value of the second card, and if it's an ace calculate its integer value.

        Detailed:
            - Initialise empty list card_values
            - Initialse running_total to 0
            - Index into the first sublist in player_hand and get the string at position 1.
            - Get its corresponding integer value from STRINGS_TO_INTEGERS (if it's an ace its value will be 11)
            - Append that to card_values
            - Add it to running_total
            - Repeat for the second sublist.
                - This time if it's an ace its value will be:
                    11 if adding 11 to the running total does not exceed 21
                    1 otherwise


GET THE TOTAL VALUE OF EACH HAND

SHOW THE PLAYER THEIR CARDS, AS WELL AS ONE OF THE DEALER'S CARDS



Things to think about:
- What happens if the deck runs out of cards?

    
    
    
    
    
    
    
    
    
    
    
    
"""