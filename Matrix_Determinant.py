#
# How to take the determinant of a matrix --
# it is simplest to start with the smallest cases:
#     A 1x1 matrix |a| has determinant a. A 2x2 matrix
#
# |a b|
# |c d|
#
# has determinant
# ad
# bc.
#
# The determinant of an n x n sized matrix is calculated by reducing
# the problem to the calculation of the determinants of n n-1 x n-1 matrices.
# For the 3x3 case, [[a, b, c], [d, e, f], [g, h, i]] or
#
# |a b c|
# |d e f|
# |g h i|
#
# the determinant is: a * det(a_minor) - b * det(b_minor) + c * det(c_minor)
# where det(a_minor) refers to taking the determinant of the 2x2 matrix created by
# crossing out the row and column in which the element a occurs, or
#
# |e f|
# |h i|
#
#
# The determinant of larger matrices are calculated analogously,
# e.g. if M is a 4x4 matrix with first row [a, b, c, d], det(M) = a * det(a_minor) - b * det(b_minor)
# + c * det(c_minor) - d * det(d_minor)


import numpy as np

ROUND_N_DIGITS = 4


def integerize_where_possible(r):
    if int(float(r)) == r:
        return int(r)
    return r

def determinant(matrix):
    r= np.linalg.det(matrix)
    r = round(r, ROUND_N_DIGITS)
    return integerize_where_possible(r)


import unittest
class TestFirst(unittest.TestCase):
    def testFirst(self):
        test = self
        Test = self
        test.assert_equals = Test.assertEqual
        Test.assert_equals = Test.assertEqual
        Test.expect = Test.assertTrue
        m1 = [ [1, 3], [2,5]]
        m2 = [ [2,5,3], [1,-2,-1], [1, 3, 4]]

        Test.assert_equals(determinant([[1]]), 1, "Determinant of a 1 x 1 matrix yields the value of the one element")
        Test.assert_equals(determinant([[5]]), 5)
        Test.assert_equals(determinant(m1), -1, "Should return 1 * 5 - 3 * 2, i.e., -1 ")
        print determinant(m2)
        Test.expect(determinant(m2) == -20)