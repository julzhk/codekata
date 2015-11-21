"""
Given a sentence with long words, 'abbreviate' them by omitting the middle letters and
replacing them with a count of the number of missing letters.
"""

import re

STRING_REPLACEMENT_TEMPLATE = '%(init)s%(len)d%(end)s'
REPLACE_LENGTH = 4


def split_words(src_string):
    """
    Split a sentence at the word boundaries
    :param src_string: String
    :return: list of words in the string
    """
    r = re.findall(r"[\w]+", src_string)
    return r


def abbreviate_word(s):
    """
    Given a string if it's longer than 4 characters,
    replace middle letters with count of the missing fragment
    :param s: String
    :return: String
    """
    if len(s) >= REPLACE_LENGTH:
        return STRING_REPLACEMENT_TEMPLATE % {'init': s[0],
                                           'len': len(s) - 2,
                                           'end': s[-1]}
    return s


def abbreviate(s):
    """
    Given a sentence replace middle of long words with a char count of the omitted
    :param s: String
    :return: String
    """
    r = s
    for word in split_words(s):
        r = r.replace(word, abbreviate_word(word))
    return r


import unittest


class TestFirst(unittest.TestCase):
    def test_first(self):
        self.assertEqual(abbreviate("1234"), '124')
        self.assertEqual(abbreviate("12345"), '135')
        self.assertEqual(abbreviate("internationalization"), 'i18n')
        self.assertEqual(abbreviate("accessibility"), 'a11y')
        self.assertEqual(abbreviate("Accessibility"), 'A11y')
        self.assertEqual(abbreviate("elephant-ride"), 'e6t-r2e')
        self.assertEqual(abbreviate("doggy-is: balloon, mat."), 'd3y-is: b5n mat')
