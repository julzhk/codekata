"""
Implement a scoring mechanism for a game of the battle of GOOD vs EVIL
Each unit in the battle has a strength score;
there can be multiple units of the same type
highest sum wins
"""


BAD_WINS = "Battle Result: Evil eradicates all trace of Good"
GOOD_WINS = "Battle Result: Good triumphs over Evil"
DRAW = "Battle Result: No victor on this battle field"
GOOD_WEIGHTS = [1, 2, 3, 3, 4, 10]
BAD_WEIGHTS = [1, 2, 2, 2, 3, 5, 10]


def calc_score(make_up, weights):
    zipped = zip(make_up, weights)
    scores = [int(a) * int(b) for (a, b) in zipped]
    return sum(scores)


def goodVsEvil(good, evil):
    goodscore = calc_score(good.split(' '), GOOD_WEIGHTS)
    badscore = calc_score(evil.split(' '), BAD_WEIGHTS)
    if goodscore == badscore:
        return DRAW
    return GOOD_WINS if goodscore > badscore else BAD_WINS


import unittest


class TestStringMethods(unittest.TestCase):
    def test_first(self):
        # Test.expect( goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1') ==
        # 'Battle Result: Evil eradicates all trace of Good', 'Evil should win' );
        self.assertEqual(goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1'), BAD_WINS)
        # Test.expect( goodVsEvil('0 0 0 0 0 10', '0 1 1 1 1 0 0') ==
        # 'Battle Result: Good triumphs over Evil', 'Good should win' );
        self.assertEqual(goodVsEvil('0 0 0 0 0 10', '0 1 1 1 1 0 0'), GOOD_WINS)
        # Test.expect( goodVsEvil('1 0 0 0 0 0', '1 0 0 0 0 0 0') ==
        # 'Battle Result: No victor on this battle field', 'Should be a tie' );
        self.assertEqual(goodVsEvil('1 0 0 0 0 0', '1 0 0 0 0 0 0'), DRAW)
