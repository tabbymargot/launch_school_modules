""" 
PROBLEM
Restate in my words
The program needs to output either the lowest ranking or highest ranking card in the list.

Inputs 
List of card constructors with rank and suit arguments

Outputs
Card object with its attributes?

EXPLICIT / IMPLICIT REQUIREMENTS
Clarifying questions
Where are all the card objects stored?
Edge cases

DATA STRUCTURES
Some way of comparing the cards_list of different card objects. Class variable referencing a list?

ALGORITHM - STFC
High level
Get the ranks of all the cards. Create a method to return the card with the min value, and the one with the max value.

Alternative High Level?
Actual algorithm
"""


class Card:
    RANKS = {
        "Jack": 11,
        "Queen": 12,
        "King": 13,
        "Ace": 14,
    }

    def __init__(self, rank, suit):
        if type(rank) != str:
            self.score = rank
        else:
            self.score = Card.RANKS[rank]
        self.rank = rank
        self.suit = suit

    def __lt__(self, other):
        return self.score < other.score
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.score}, '{self.suit}')"
    
    def __eq__(self, other):
        return repr(self) == repr(other)
    
    def __str__(self):
        rank = self.rank if self.score in Card.RANKS.values() else self.score
        return f"{rank} of {self.suit}"


cards = [Card(2, 'Hearts'),
        Card('Ace', 'Clubs')]

print(min(cards) == Card(2, 'Hearts'))             # True
print(max(cards) == Card('Ace', 'Clubs'))          # True
print(str(min(cards)) == "2 of Hearts")            # True
print(str(max(cards)) == "Ace of Clubs")           # True

cards = [Card(5, 'Hearts')]
print(min(cards) == Card(5, 'Hearts'))             # True
print(max(cards) == Card(5, 'Hearts'))             # True
print(str(Card(5, 'Hearts')) == "5 of Hearts")     # True

cards = [Card(4, 'Hearts'),
         Card(4, 'Diamonds'),
         Card(10, 'Clubs')]
print(min(cards).rank == 4)                        # True
print(max(cards) == Card(10, 'Clubs'))             # True
print(str(Card(10, 'Clubs')) == "10 of Clubs")     # True

cards = [Card(7, 'Diamonds'),
         Card('Jack', 'Diamonds'),
         Card('Jack', 'Spades')]
print(min(cards) == Card(7, 'Diamonds'))           # True
print(max(cards).rank == 'Jack')                   # True
print(str(Card(7, 'Diamonds')) == "7 of Diamonds") # True

cards = [Card(8, 'Diamonds'),
         Card(8, 'Clubs'),
         Card(8, 'Spades')]
print(min(cards).rank == 8)                        # True
print(max(cards).rank == 8)                        # True