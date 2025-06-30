""" # Include Card and Deck classes from the last two exercises. """
import random

ALL_RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]

class Card:
    VALUES = {"Jack": 11, "Queen": 12, "King": 13, "Ace": 14}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    @property
    def value(self):
        return Card.VALUES.get(self.rank, self.rank)

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

    def __init__(self):
        self.cards = None
        self.reset()

    def reset(self):
        self.cards =    [Card(rank, suit)
                        for suit in Deck.SUITS
                        for rank in Deck.RANKS
                        ]
        
        random.shuffle(self.cards)

    def draw(self):
        if not self.cards:
            self.reset()

        return self.cards.pop(0)

class PokerHand:
    # FULL_DECK = 52
    NUMBER_OF_CARDS = 5 

    def __init__(self, deck):
        self.cards = [deck.draw() for _ in range(PokerHand.NUMBER_OF_CARDS)]
    
    def print(self):
        for card in self.cards:
            print(str(card) )

    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
          return "High card"
        
    def hand_contains_one_suit(self, suits):
        return len(suits) == 1
    
    def get_all_straights(self):
        return  [
                    set(ALL_RANKS[idx: idx + 5])
                    for idx in range(len(ALL_RANKS))
                ]
    
    def sort_ranks(self, cards):
        return sorted([str(card.rank) for card in cards])
    
    def split_into_three_and_two(self):
        first_three = self.sort_ranks(self.cards)[:3]
        last_two = self.sort_ranks(self.cards)[3:]

        return first_three, last_two

    def first_three_are_equal(self, ranks):
        if all([True if rank == ranks[0] else False for rank in ranks]):
            return True
        
    def last_two_are_equal(self, ranks):
        if (ranks[0] == ranks[1]):
            return True
        
    def get_ranks_as_list(self):
        return [card.rank for card in self.cards]
        
    def get_number_of_pairs(self, ranks):
        is_in_a_pair = []
        seen = []

        for rank in ranks:
            if (ranks.count(rank) == 2) and (rank not in seen):
                is_in_a_pair.append(rank)
                seen.append(rank)

        return len(is_in_a_pair)
    
    def get_ranks_and_suits_as_sets(self):
        ranks = set()
        suits = set()

        for card in self.cards:
            ranks.add(card.rank)
            suits.add(card.suit)

        return(ranks, suits)

    def _is_royal_flush(self):
        straight = {"Ace", "Queen", "King", "Jack", 10}
        ranks, suits = self.get_ranks_and_suits_as_sets()

        if (ranks == straight) and self.hand_contains_one_suit(suits):
            return True

    def _is_straight_flush(self):
        ranks, suits = self.get_ranks_and_suits_as_sets()

        if  (ranks in self.get_all_straights()) and \
            self.hand_contains_one_suit(suits):
            return True

    def _is_four_of_a_kind(self):
        ranks = [card.rank for card in self.cards]

        for rank in ranks:
            if ranks.count(rank) == 4:
                return True

    def _is_full_house(self):
        first_three, last_two = self.split_into_three_and_two()

        if  self.first_three_are_equal(first_three) and \
            self.last_two_are_equal(last_two):
            return True

    def _is_flush(self):
        suits = set()

        for card in self.cards:
            suits.add(card.suit)

        if self.hand_contains_one_suit(suits):
            return True

    def _is_straight(self):
        ranks, suits = self.get_ranks_and_suits_as_sets()

        if  (ranks in self.get_all_straights()) and \
            (not self.hand_contains_one_suit(suits)):
            return True

    def _is_three_of_a_kind(self):
        first_three, last_two = self.split_into_three_and_two()

        if  self.first_three_are_equal(first_three) and \
            (not self.last_two_are_equal(last_two)):
            return True

    def _is_two_pair(self):
        ranks = self.get_ranks_as_list()

        if self.get_number_of_pairs(ranks) == 2:
            return True

    def _is_pair(self):
        ranks = self.get_ranks_as_list()

        if self.get_number_of_pairs(ranks) == 1:
            return True


# hand = PokerHand(Deck())
# hand.print()
# print(hand.evaluate())
# print()


# Adding TestDeck class for testing purposes

class TestDeck(Deck):
    def __init__(self, cards):
        self._deck = cards

    def draw(self):
        return self._deck.pop(0)

# All of these tests should return True

hand = PokerHand(
    TestDeck(
        [
            Card("Ace", "Hearts"),
            Card("Queen", "Hearts"),
            Card("King", "Hearts"),
            Card("Jack", "Hearts"),
            Card(10, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Royal flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Clubs"),
            Card("Queen", "Clubs"),
            Card(10, "Clubs"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight flush")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)

print(hand.evaluate() == "Four of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Full house")

hand = PokerHand(
    TestDeck(
        [
            Card(10, "Hearts"),
            Card("Ace", "Hearts"),
            Card(2, "Hearts"),
            Card("King", "Hearts"),
            Card(3, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Diamonds"),
            Card(10, "Clubs"),
            Card(7, "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card("Queen", "Clubs"),
            Card("King", "Diamonds"),
            Card(10, "Clubs"),
            Card("Ace", "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(6, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Three of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(9, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(8, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Two pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card("King", "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "High card")