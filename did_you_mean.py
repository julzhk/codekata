"""I'm sure, you know Google's "Did you mean ...?", when you entered a search term and mistyped a word.
In this kata we want to implement something similar.
You'll get an entered term (lowercase string) and an array of known words (also lowercase strings).

Your task is to find out which word from the dictionary is most similar to the entered one.
The similarity is described by the minimum number of letters you have to add, remove or replace
in order to get from the entered word to one of the dictionary. The lower the number of required changes,
the higher the similarity between each two words.

Same words are obviously the most similar ones.

A word that needs one letter to be changed is more similar to another word that needs 2 (or more) letters
to be changed. E.g. the mistyped term berr is more similar to beer (1 letter to be replaced)
than to barrel (3 letters to be changed in total).
Extend the dictionary in a way that it is able to return you the most similar word from the list of known words.


there is always exactly one possible solution
"""

from itertools import combinations


class Dictionary:
    def __init__(self, words):
        self.words = words

    def find_most_similar(self, term):
        scores = {word: self.find_score(term, word) for word in self.words}
        return min(scores, key=scores.get)

    @staticmethod
    def insert_str_in_str(source, loc, insert_str=' '):
        """
        :param source: string 'abcd'
        :param loc: integer 2
        :param insert_str: string ' '
        :return: 'ab cd'
        """
        return '%s%s%s' % (source[:loc],
                           insert_str,
                           source[loc:]
                           )

    def find_score(self, a, b):
        longstr, shortstr = (a, b) if len(a) > len(b) else (b, a)
        len_diff = abs(len(longstr) - len(shortstr))
        max_len = len(longstr)
        scores = []
        for space_locs in combinations(range(max_len), len_diff):
            s = self.create_string_candidate(shortstr, space_locs)
            scores.append(self.calculate_score(longstr, s))
        return min(scores)

    def create_string_candidate(self, src_str, space_locs):
        """
        Given a string and an iterable of locations to insert strings into, return string with insertions
        :param src_str: 'abcd'
        :param space_locs: [1,3]
        :return: 'a b cd'
        """
        s = src_str
        for space_loc in space_locs:
            s = self.insert_str_in_str(s, space_loc)
        return s

    @staticmethod
    def calculate_score(a, b):
        score = 0
        for i in range(0, max(len(a), len(b))):
            if a[i] != b[i]:
                score += 1
        return score


import unittest


class TestFirst(unittest.TestCase):
    def test_fn(self):
        test = self
        Test = self
        test.assert_equals = Test.assertEqual
        Test.assert_equals = Test.assertEqual

        words = ['ruby', 'javascript', 'brainfuck', 'php', 'cpp', 'coffeescript', 'java', 'python', 'c']
        test_dict = Dictionary(words)
        Test.assert_equals(test_dict.find_most_similar('heaven'), 'java')
        Test.assert_equals(test_dict.find_score('apple', 'apple'), 0)
        Test.assert_equals(test_dict.find_score('appla', 'apple'), 1)
        Test.assert_equals(test_dict.find_score('appl', 'apple'), 1)
        words = ['cherry', 'peach',
                 'pineapple', 'melon',
                 'strawberry', 'raspberry',
                 'apple', 'coconut',
                 'banana']
        test_dict = Dictionary(words)
        Test.assert_equals(test_dict.find_most_similar('strawbery'), 'strawberry')
        Test.assert_equals(test_dict.find_most_similar('aple'), 'apple')
        Test.assert_equals(test_dict.find_most_similar('berry'), 'cherry')
