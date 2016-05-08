"""
Write a function that takes a number or a string
and returns number of permutations

For example, starting with:

45 has 2 permutations (45,54)
115 has 3 (115,151,511)
ie:
perms(1)==1
perms(45)==2
perms(115)==3
perms("abc")==6
"""

from itertools import permutations
from math import factorial

def naive_perms(s):
    s = list(s)
    r = set((permutations(s)))
    return len(r)

def perms(element):
    s = str(element)
    if len(set(s)) == len(list(s)):
        # every char is different so simple optimization:
        # answer is just factorial:
        return factorial(len(s))
    else:
        # factorial - repeated chars ..
        return naive_perms(s)


import unittest
class TestFirst(unittest.TestCase):
    def testFirst(self):
        test = self
        Test = self
        test.assert_equals = Test.assertEqual
        Test.assert_equals = Test.assertEqual

        Test.assert_equals(perms(2), 1)
        Test.assert_equals(perms(25), 2)
        Test.assert_equals(perms(342), 6)
        Test.assert_equals(perms(1397), 24)
        Test.assert_equals(perms(76853), 120)
        Test.assert_equals(perms("a"), 1)
        Test.assert_equals(perms("ab"), 2)
        Test.assert_equals(perms("abc"), 6)
        Test.assert_equals(perms(737), 3)
        Test.assert_equals(perms(66666), 1)