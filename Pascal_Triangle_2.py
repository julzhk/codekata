"""
Given a height, return a Pascal's triangle
"""

import unittest

def pascal_row(row):
    if len(row) == 1:
        return [row[0],row[0]]
    new = [1]
    for val in range(1,len(row)):
        new.append(row[val-1] + row[val])
    new.append(1)
    return new


def pascal(p):
    current_row = [1]
    r = [current_row]
    for row in xrange(1,p):
        current_row = pascal_row(current_row)
        r.append(current_row)
    return r

class TestFirst(unittest.TestCase):
    def test_first(self):
        test = self
        test.assert_equals = self.assertEqual
        Test = self
        Test.assert_equals = self.assertEqual

        test.assert_equals(pascal_row([1]), [1,1])
        test.assert_equals(pascal_row([1,1]), [1,2, 1])
        test.assert_equals(pascal_row([1,2, 1]), [1,3,3, 1])
        test.assert_equals(pascal_row([1,3,3,1]), [1,4,6,4,1])
        test.assert_equals(pascal(1), [[1]])
        test.assert_equals(pascal(5), [
                                        [1],
                                        [1,1],
                                        [1,2,1],
                                        [1,3,3,1],
                                        [1,4,6,4,1]
                                        ])