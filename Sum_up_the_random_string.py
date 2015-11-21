"""
What is the sum of all digits in a string?
"""

import re


def sum_from_string(string):
    numbers = re.findall('\d+', string)
    return sum([int(i) for i in numbers])


import unittest


class TestFirst(unittest.TestCase):
    def test_first(self):
        # test.assert_equals(sum_from_string("In 2015, I want to know how much does iPhone 6+ cost?"),2021)
        self.assertEqual(sum_from_string("In 2015, I want to know how much does iPhone 6+ cost?"), 2021)
        self.assertEqual(sum_from_string("In -2015, I want to know how much does iPhone 6+ cost?"), 2021)
        # test.assert_equals(sum_from_string("1+1=2"),4)
        self.assertEqual(sum_from_string("1+1=2"), 4)
        # test.assert_equals(sum_from_string("e=mc^2"),2)
        self.assertEqual(sum_from_string('e=mc^2'), 2)
