"""
Convert a string into a string of alphabetic positions
"""

A_CODE_OFFSET = ord('a')

def get_char_code(c, a_code=A_CODE_OFFSET):
    c = ord(c.lower())
    return str(c - a_code + 1)


def is_in_alphabet(c):
    return 'a' <= c.lower() <= 'z'


def alphabet_position(text):
    codes = [get_char_code(c) for c in text if is_in_alphabet(c)]
    return ' '.join(codes)


import unittest


class TestFirst(unittest.TestCase):
    def test_first(self):
        from random import randint

        test = self
        test.assert_equals = self.assertEqual
        test.assert_equals(alphabet_position("The sunset sets at twelve o' clock."),
                           "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
        test.assert_equals(alphabet_position("The narwhal bacons at midnight."),
                           "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")

        number_test = ""
        for item in range(10):
            number_test += str(randint(1, 9))
        test.assert_equals(alphabet_position(number_test), "")
