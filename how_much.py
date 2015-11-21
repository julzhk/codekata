"""
I always thought that my old friend John was rather richer than he looked
but I never knew exactly how much money he actually had. One day (as I was plying him with questions)
he said: "Imagine I have between m and n Zloty (or did he say Quetzal? I can't remember!)

If I were to buy 9 cars costing C each, I'd only have 1 Zlotty (or was it Meticals?) left.

If I were to buy 7 boats at B each, I'd only have 2 Ringglets (or was it Zlotty?) left.

Could you tell me in each possible case:

how much money he could possibly have
the cost c of a car
the cost b of a boat?
So, I will have a better idea about his fortune.
Note that if m-n is big enough, you might havea lot of possible answers.

Each answer will be given as ["M: f", "B: b", "C: c"]
and all the answers as
[ ["M: f", "B: b", "C: c"] ... ]. M stands for "Money", B for boats, C for cars.

m and n are positive or null integers with m <= n or m >= n, m and n inclusive.
"""
from math import floor

BOAT_PRICE = 7
CAR_PRICE = 9


def get_number_cars(cash):
    return floor((cash - 1.0) / CAR_PRICE)


def get_number_boats(cash):
    return floor((cash - 2.0) / BOAT_PRICE)


def is_satified(cars_count, boats_count, cash):
    """
    Do the variables satisfy the problem?
    """
    return (cars_count * CAR_PRICE) + 1 == cash == (boats_count * BOAT_PRICE) + 2


def howmuch(m, n):
    solutions = []
    for cash in range(min([m, n + 1]), max([m, n + 1])):
        boats_count = get_number_boats(cash)
        cars_count = get_number_cars(cash)
        if is_satified(cars_count=cars_count,
                       boats_count=boats_count,
                       cash=cash
                       ):
            solutions.append(["M: %d" % cash,
                              "B: %d" % boats_count,
                              "C: %d" % cars_count
                              ])
    return solutions


import unittest


class TestFirst(unittest.TestCase):
    def test_first(self):
        test = self
        Test = self
        test.assert_equals = Test.assertEqual
        Test.assert_equals = Test.assertEqual
        test.assert_equals(howmuch(2950, 2950), [])
        test.assert_equals(howmuch(20000, 20100), [
            ["M: 20008", "B: 2858", "C: 2223"],
            ["M: 20071", "B: 2867", "C: 2230"]])
        test.assert_equals(howmuch(1, 100), [
            ["M: 37", "B: 5", "C: 4"],
            ["M: 100", "B: 14", "C: 11"]
        ])
        test.assert_equals(howmuch(1000, 1100), [["M: 1045", "B: 149", "C: 116"]])
        test.assert_equals(howmuch(10000, 9950), [
            ["M: 9991", "B: 1427", "C: 1110"]
        ]
                           )
        test.assert_equals(howmuch(0, 200), [["M: 37", "B: 5", "C: 4"],
                                             ["M: 100", "B: 14", "C: 11"],
                                             ["M: 163", "B: 23", "C: 18"]
                                             ]
                           )