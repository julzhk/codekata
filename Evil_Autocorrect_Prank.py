"""
Implement a function that replaces 'U'/'you' with 'your sister'
Handle duplicate 'u's smartly.
"""

import re

TARGET = 'u'
TOKEN = '*'
REPLACE_STRING = 'your sister'

# def autocorrect(input):
# Alternative with regexes!
#     return re.sub(r'(?i)\b(u|you+)\b', "your sister", input)

def autocorrect(input_string):
    for search_target in ['u', 'you']:
        input_string = replace_target_alone(input_string, search_target)
        input_string = replace_startswith_target(input_string, search_target)
        input_string = replace_endswith_target(input_string, search_target)
        input_string = replace_target_is_substring(input_string, search_target)
    input_string = replace_multiple_uuu_case(input_string)
    return input_string.replace(TOKEN, REPLACE_STRING)


def replace_multiple_uuu_case(input_string):
    regex_target = re.compile(r"^(.*)you(?:u+)(.*)$", re.IGNORECASE)
    input_string = re.sub(regex_target, r'\1%s\2' % TOKEN, input_string)
    return input_string


def replace_target_is_substring(input_string, search_target):
    regex_target = re.compile(r'\b%s\b' % search_target, re.IGNORECASE)
    input_string = re.sub(regex_target, TOKEN, input_string)
    return input_string


def replace_endswith_target(input_string, search_target):
    regex_target = re.compile(r'(.*)\s%s([!|?|\.|"|\']*)$' % search_target, re.IGNORECASE)
    input_string = re.sub(regex_target, r"\1 %s\2" % TOKEN, input_string)
    return input_string


def replace_startswith_target(input_string, search_target):
    regex_target = re.compile(r'^%s\s(.*)' % search_target, re.IGNORECASE)
    input_string = re.sub(regex_target, r"%s \1" % TOKEN, input_string)
    return input_string


def replace_target_alone(input_string, search_target):
    regex_target = re.compile(r'^%s$' % search_target, re.IGNORECASE)
    input_string = re.sub(regex_target, TOKEN, input_string)
    return input_string


import unittest


class TestStringMethods(unittest.TestCase):
    def test_first(self):
        self.assertEqual(autocorrect("u"), "your sister")
        self.assertEqual(autocorrect("u abc"), "your sister abc")
        self.assertEqual(autocorrect("U abc"), "your sister abc")
        self.assertEqual(autocorrect("abc u"), "abc your sister")
        self.assertEqual(autocorrect("abc U"), "abc your sister")
        self.assertEqual(autocorrect("U"), "your sister")
        self.assertEqual(autocorrect("abc u def"), "abc your sister def")
        self.assertEqual(autocorrect("abc U def"), "abc your sister def")
        self.assertEqual(autocorrect("you"), "your sister")
        self.assertEqual(autocorrect("you you"), "your sister your sister")
        self.assertEqual(autocorrect("you youuuu"), "your sister your sister")
        self.assertEqual(autocorrect("YOU"), "your sister")
        self.assertEqual(autocorrect("youuuuu"), "your sister")
        self.assertEqual(autocorrect("Youuuuu"), "your sister")
        self.assertEqual(autocorrect("Youuuuu abc"), "your sister abc")
        self.assertEqual(autocorrect("you tube"), "your sister tube")
        self.assertEqual(autocorrect("youtube"), "youtube")
        self.assertEqual(autocorrect("I miss you!"), "I miss your sister!")
        self.assertEqual(autocorrect("I miss you."), "I miss your sister.")
        self.assertEqual(autocorrect("I miss you!'"), "I miss your sister!'")
        self.assertEqual(autocorrect("I miss you!!!'"), "I miss your sister!!!'")
        self.assertEqual(autocorrect('I miss you!!!"'), 'I miss your sister!!!"')
        self.assertEqual(autocorrect('u u youville utube u youyouyou'),
                                     'your sister your sister youville utube your sister youyouyou')
        self.assertEqual(autocorrect('u u youville utube your sister youyouyou uuu raiyou united your sister your sister your sister'),
                                     'your sister your sister youville utube your sister youyouyou uuu raiyou united your sister your sister your sister')
