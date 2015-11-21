"""
Implement a function to identify duplicate numbers in a list using a set
todo: use Counter
"""


def find_dup(arr):
    seen = set()
    for i in arr:
        if i not in seen:
            seen.add(i)
        else:
            return i


import unittest


class TestFirst(unittest.TestCase):
    def test_first(self):
        test = self
        Test = self
        test.assert_equals = Test.assertEqual
        Test.assert_equals = Test.assertEqual

        Test.assert_equals(find_dup([1, 1, 2, 3]), 1)
        Test.assert_equals(find_dup([1, 2, 2, 3]), 2)
        Test.assert_equals(find_dup([5, 4, 3, 2, 1, 1]), 1)
        Test.assert_equals(find_dup([1, 3, 2, 5, 4, 5, 7, 6]), 5)
        Test.assert_equals(find_dup([8, 2, 6, 3, 7, 2, 5, 1, 4]), 2)
