"""
Given 2 points find the slope of the line between them.
"""


UNDEFINED_SLOPE = "undefined"


def calculate_slope(x1, x2, y1, y2):
    return (y2 - y1) / (x2 - x1)


def find_slope(points):
    x1, y1, x2, y2 = points
    try:
        r = calculate_slope(x1, x2, y1, y2)
        return str(r)
    except ZeroDivisionError:
        return UNDEFINED_SLOPE


import unittest


class TestFirst(unittest.TestCase):
    def test_first(self):
        test = self
        Test = self
        test.assert_equals = Test.assertEqual
        Test.assert_equals = Test.assertEqual
        test.assert_equals(find_slope([19, 3, 20, 3]), "0")
        test.assert_equals(find_slope([-7, 2, -7, 4]), "undefined")
        test.assert_equals(find_slope([10, 50, 30, 150]), "5")
        test.assert_equals(find_slope([10, 20, 20, 80]), "6")
        test.assert_equals(find_slope([-10, 6, -10, 3]), "undefined")
