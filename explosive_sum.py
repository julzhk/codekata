"""
How many ways to add up to a value?
2 can only be 1+1.
3 can be 1+2 or 2+1
4 can be made up of threes, twos and ones in 5 ways:

from wikipedia: https://en.wikipedia.org/wiki/Partition_(number_theory)#

In number theory and combinatorics, a partition of a positive integer n,
 also called an integer partition, is a way of writing n as a sum of positive integers.
 Two sums that differ only in the order of their summands are considered the same partition.
 If order matters, the sum becomes a composition.
  For example, 4 can be partitioned in five distinct ways:

4
3 + 1
2 + 2
2 + 1 + 1
1 + 1 + 1 + 1
"""

from itertools import product,combinations


def combinations_with_replacement(iterable, r, total):
    n = len(iterable)
    for indices in product(range(n), repeat=r):
        if sorted(indices) == list(indices):
            yield tuple(iterable[i] for i in indices)


def exp_sum(n):
    r = 0
    for seq in xrange(1, n + 1):
        combos = combinations_with_replacement(xrange(1, n + 1), seq, total=n)
        solutions = (i for i in combos if sum(i) == n)
        counts = len([len(c) for c in solutions])
        r += counts
    return r


import unittest

class TestFirst(unittest.TestCase):
    def test_first(self):
        test = self
        Test = self
        test.assert_equals = Test.assertEqual
        Test.assert_equals = Test.assertEqual

        test.assert_equals(exp_sum(-1), 0)
        test.assert_equals(exp_sum(0), 0)
        test.assert_equals(exp_sum(1), 1)
        test.assert_equals(exp_sum(2), 2)
        test.assert_equals(exp_sum(3), 3)

        test.assert_equals(exp_sum(4), 5)
        test.assert_equals(exp_sum(5), 7)
        # test.assert_equals(exp_sum(10), 42)
        # test.assert_equals(exp_sum(50), 204226)
        # test.assert_equals(exp_sum(80), 15796476)
        # test.assert_equals(exp_sum(100), 190569292)



