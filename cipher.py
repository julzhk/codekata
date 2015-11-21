"""
Implement a simple rotations cypher
"""

map1 = "abcdefghijklmnopqrstuvwxyz"
map2 = "etaoinshrdlucmfwypvbgkjqxz"

class Cipher(object):
    def __init__(self, map1, map2):
        self.inmap = map1
        self.outmap = map2


    def code(self, string,frommap,tomap):
        r = ''
        for s in string:
            try:
                r += tomap[frommap.index(s)]
            except (ValueError, KeyError):
                r += s
        return r


    def encode(self, string):
        return self.code(string=string,
                         frommap=self.inmap,
                         tomap=self.outmap
                         )

    def decode(self, string):
        return self.code(string=string,
                         frommap=self.outmap,
                         tomap=self.inmap
                         )


import unittest


class TestFirst(unittest.TestCase):
    def test_first(self):
        map1 = "abcdefghijklmnopqrstuvwxyz"
        map2 = "etaoinshrdlucmfwypvbgkjqxz"
        cipher = Cipher(map1, map2)
        self.assertEqual(cipher.encode("abc"), "eta")
