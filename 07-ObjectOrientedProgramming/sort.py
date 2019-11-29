class Card(object):

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        return self.rank < other.rank

hand = [Card(10, 'H'), Card(2, 'h'), Card(12, 'h'), Card(13, 'h'), Card(14, 'h')]
hand_order = [c.rank for c in hand]  # [10, 2, 12, 13, 14]

hand_sorted = sorted(hand)
hand_sorted_order = [c.rank for c in hand_sorted]  # [2, 10, 12, 13, 14]

hand.sort()
hand_sort = [c.rank for c in hand]  # [10, 2, 12, 13, 14]
