import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class Deck(object):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self, numberofdecks=1):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks
                                        for deck in xrange(0,numberofdecks)
                       ]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


from unittest import TestCase


class testcarddesk(TestCase):

    def test_simplecards(self):
        beer_card = Card('7', 'diamonds')
        self.assertEquals(beer_card,Card(rank='7', suit='diamonds'))

    def test_deck(self):
        deck = Deck()
        self.assertEquals(len(deck),52)
        self.assertEquals(deck[:3],
                          [Card(rank='2', suit='spades'),
                           Card(rank='3', suit='spades'),
                           Card(rank='4', suit='spades')])
        self.assertEquals(deck[12::13],[Card(rank='A', suit='spades'),
                                        Card(rank='A', suit='diamonds'),
                                        Card(rank='A', suit='clubs'),
                                        Card(rank='A', suit='hearts')]
                          )
        self.assertEquals(Card('Q', 'hearts') in deck, True)

    def test_multipledecks(self):
        # allow for multiple 52 card decks
        self.assertEquals(len(Deck(2)),52 * 2)