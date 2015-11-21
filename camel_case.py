"""
Convert a variable into camelcase (remove dashes etc)
"""

def split_by_char(text, split_char):
    return text.split(split_char)


def capitalize(word):
    return word[0].capitalize() + word[1:]


def capitalize_list(text_list):
    return [capitalize(c) for c in text_list]


def join_up_list(text_list):
    return ''.join(text_list)


def to_camel_case_with_split(text, splitchar='-'):
    text = split_by_char(text, splitchar)
    return text[0] + join_up_list(capitalize_list(text[1:]))


def to_camel_case(text):
    text = to_camel_case_with_split(text, splitchar='-')
    text = to_camel_case_with_split(text, splitchar='_')
    return text




import unittest


class TestFirst(unittest.TestCase):
    def test_first(self):
        test = self
        Test = self
        test.assert_equals = Test.assertEqual
        Test.assert_equals = Test.assertEqual
        # test.assert_equals(to_camel_case(''), '', "An empty string was provided but not returned")
        print to_camel_case("the_stealth_warrior")
        test.assert_equals(to_camel_case("the_stealth_warrior"), "theStealthWarrior", "to_camel_case('the_stealth_warrior') did not return correct value")
        test.assert_equals(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior", "to_camel_case('The-Stealth-Warrior') did not return correct value")
        test.assert_equals(to_camel_case("A-B-C"), "ABC", "to_camel_case('A-B-C') did not return correct value")
        test.assert_equals(to_camel_case("the-Pippi-Was_evil"), "thePippiWasEvil")
        print to_camel_case("A-Cat_was-cute")
        test.assert_equals(to_camel_case("A-Cat_was-cute"), "ACatWasCute")

        # to_camel_case(the-Pippi-Was_evil) did not return correct value: 'the-Pippi-WasEvil' should equal 'thePippiWasEvil'
