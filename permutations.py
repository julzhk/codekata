"""
Given a string, what permutations of the component strings are there?
"""

from itertools import permutations as perm

def permutations(s):
    """
>permutations('aab')
{'aab', 'aba', 'baa'}
>permutations('aaba')
{'aaab', 'aaba', 'abaa', 'baaa'}
>permutations('abc')
{'abc', 'acb', 'bac', 'bca', 'cab', 'cba'}
    :param s: string
    :return: set of permutations
    """
    r = perm(s)
    return set([''.join(i) for i in r])


import unittest
class TestFirst(unittest.TestCase):
    def testFirst(self):
        test = self
        Test = self
        test.assert_equals = Test.assertEqual
        Test.assert_equals = Test.assertEqual
        Test.assert_equals(sorted(permutations('a')), ['a']);
        Test.assert_equals(sorted(permutations('ab')), ['ab', 'ba'])
        Test.assert_equals(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
