# coding=utf-8

# Kata: Simulate the game 'SNAP!'
# Features:
#  - Allow variable number of standard 52-card decks
#  - Allow for several 'matching' conditions: either match just suit, or just rank, or match on both.

# ----

# Thanks to (awesome!) 'Fluent Python' book for inspiration for the Deck class.
# see: Fluent Python by Luciano Ramalho (O’Reilly).
# Copyright 2015 Luciano Ramalho, 978-1-491-94600-8.
# and
# https://github.com/fluentpython/example-code

from collections import  namedtuple, defaultdict
from random import shuffle, choice

# We're going to monkey patch a 'Card' namedtuple with these methods
def suitequals(card1, card2):
    return card1.suit == card2.suit

def rankequals(card1,card2):
    return card1.rank== card2.rank

def cardequal(card1, card2):
    return suitequals(card1, card2) and rankequals(card1,card2)

def cardrepr(card):
    return '{}, suit: {}'.format(card.rank, card.suit)

Card = namedtuple('Card', ['deck', 'rank', 'suit'])
Card.__eq__ = cardequal
Card.__repr__ = cardrepr

class Deck(object):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self, numberofdecks=1):
        self._cards = [Card(deck, rank, suit)
                                        for suit in self.suits
                                        for rank in self.ranks
                                        for deck in xrange(0,numberofdecks)
                       ]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, card):
        self._cards[position] = card

def main():
    number_of_decks = initialize_game()
    players = ['p1','p2']
    no_players = len(players)
    scores = defaultdict(int)
    deck = Deck(numberofdecks=number_of_decks)
    shuffle(deck)
    prev_indx = - no_players
    # use slicing to step thru N at a time
    for indx in range(0,len(deck))[::no_players]:
        print '.',
        if deck[indx] == deck[indx + 1]:
            print 'top cards: {} & {}'.format(deck[indx], deck[indx + 1])
            round_has_winner(indx, players, prev_indx, scores)
            prev_indx = indx
    final_scores(players, scores)


def initialize_game():
    try:
        n = raw_input('number of card decks?')
        n = abs(int(n))
    except ValueError:
        n = 3
        print 'default: three packs'
    card_winning_condition_key = raw_input('How do you win a hand? \n\n'
                                           '0:Card exact match \n'
                                           '1:Card rank match \n'
                                           '2:Card suit match \n'
                                           )
    cardequalscondition = {
        0: cardequal,
        1: rankequals,
        2: suitequals
    }
    try:
        if int(card_winning_condition_key) not in cardequalscondition:
            raise ValueError
        Card.__eq__ = cardequalscondition[card_winning_condition_key]
    except ValueError:
        print 'default match: on card rank and suit'
    return n


def round_has_winner(indx, players, prev_indx, scores):
    winning_player = choice(players)
    print '   "MATCH!" says {}'.format(winning_player)
    round_score = (indx - prev_indx)
    print '   {} gained {} pts'.format(winning_player, round_score)
    scores[winning_player] += round_score
    print '   {} now has {} pts'.format(winning_player, scores[winning_player])


def final_scores(players, scores):
    print "\n\n\n\n"
    print 'final scores'
    for player in players:
        print '{} finished with {} pts'.format(player, scores[player])
    print


if __name__ == "__main__":
    main()


from unittest import TestCase

class TestCardDeck(TestCase):

    def test_simplecards_deck_not_significant(self):
        beer_card = Card(0, '7', 'diamonds')
        self.assertEquals(beer_card,
                          Card(1, rank='7', suit='diamonds'))

    def test_deck(self):
        deck = Deck()
        self.assertEquals(len(deck),52)
        self.assertEquals(deck[:3],
                          [Card(deck='1',rank='2', suit='spades'),
                           Card(deck='1',rank='3', suit='spades'),
                           Card(deck='1',rank='4', suit='spades')])
        self.assertEquals(deck[12::13],[Card(deck='1',rank='A', suit='spades'),
                                        Card(deck='1',rank='A', suit='diamonds'),
                                        Card(deck='1',rank='A', suit='clubs'),
                                        Card(deck='1',rank='A', suit='hearts')]
                          )
        self.assertEquals(Card('1','Q', 'hearts') in deck, True)

    def test_multipledecks(self):
        # allow for multiple 52 card decks
        self.assertEquals(len(Deck(2)),52 * 2)
        self.assertEquals(len(Deck(3)),52 * 3)

    def test_shuffle(self):
        # as we have added the setitem method, thus Deck iteratable now supports 'shuffle'!
        deck1 = Deck()
        deck2 = Deck()
        shuffle(deck1)
        self.assertNotEquals(deck1,deck2)

class TestCompareCards(TestCase):
    def test_exact_equals(self):
        card1 = Card(deck='1',rank='2', suit='spades')
        card2 = Card(deck='1',rank='2', suit='spades')
        self.assertEquals(card1,card2)

    def test_suit_equals(self):
        Card.__eq__ = suitequals
        card1 = Card(deck='1',rank='3', suit='spades')
        card2 = Card(deck='1',rank='2', suit='spades')
        self.assertEquals(card1,card2)

    def test_suit_not_equals(self):
        Card.__eq__ = suitequals
        card1 = Card(deck='1',rank='3', suit='hearts')
        card2 = Card(deck='1',rank='2', suit='spades')
        self.assertNotEquals(card1,card2)

    def test_rank_equals(self):
        Card.__eq__ = rankequals
        card1 = Card(deck='1',suit='3', rank='spades')
        card2 = Card(deck='1',suit='2', rank='spades')
        self.assertEquals(card1,card2)

    def test_rank_not_equals(self):
        Card.__eq__ = rankequals
        card1 = Card(deck='1',suit='3', rank='hearts')
        card2 = Card(deck='1',suit='2', rank='spades')
        self.assertNotEquals(card1,card2)

