"""
Implement a function to take firstname, lastname and perhaps middlename into a single string
(This must be much harder in other languages!)
"""

def combine_names(*args):
    return ' '.join(args)


import unittest

class TestFirst(unittest.TestCase):
    def test_first(self):
        self.assertEqual(combine_names('aaa','vvv'),'aaa vvv')
        self.assertEqual(combine_names('andy','bill','charles'),'andy bill charles')