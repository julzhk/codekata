from itertools import permutations

def deduplist(mylist):
    return list(set(mylist))

def get_words(hash_of_letters):
    source = ''
    for k in hash_of_letters:
        for letter in hash_of_letters[k]:
            source += (letter * k)
    r = []
    r += [''.join(i) for i in permutations(source)]
    r = deduplist(r)
    r.sort()
    return  r


import unittest
class TestFirst(unittest.TestCase):
    def testFirst(self):
        test = self
        Test = self
        test.assert_equals = Test.assertEqual
        Test.assert_equals = Test.assertEqual
        Test.assert_equals(get_words({1:["a", "b", "c"]}),  ["abc", "acb", "bac", "bca", "cab", "cba"],
                           "Nope! Try again.")
        Test.assert_equals(get_words({2:["a"], 1:["b", "c"]}),
                           ["aabc", "aacb", "abac", "abca", "acab",
                            "acba", "baac", "baca", "bcaa", "caab",
                            "caba", "cbaa"])