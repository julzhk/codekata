"""
Implement a function that takes compass moves and resolves them to the simples outcome of moves
"""

def dirReduc(arr):
    reduced = True
    while reduced:
        reduced = False
        if len(arr)>1:
            reduced = pop_redundant_moves(arr)
    return arr


def pop_redundant_moves(arr):
    for i in xrange(0, len(arr) - 1):
        for checklist in [("NORTH", "SOUTH"), ("EAST", "WEST")]:
            for checklist_order in [(0,1),(1,0)]:
                if arr[i] == checklist[checklist_order[0]] and \
                                arr[i + 1] == checklist[checklist_order[1]]:
                    arr.pop(i)
                    arr.pop(i)
                    return True
    return False


import unittest


class TestFirst(unittest.TestCase):

    def test_first(self):
        test = self
        test.assert_equals = self.assertEqual
        Test = self
        Test.assert_equals = self.assertEqual

        a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
        test.assert_equals(dirReduc(a), ['WEST'])
        u=["NORTH", "WEST", "SOUTH", "EAST"]
        test.assert_equals(dirReduc(u), ["NORTH", "WEST", "SOUTH", "EAST"])
