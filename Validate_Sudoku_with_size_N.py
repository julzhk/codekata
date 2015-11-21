# Sudoku is a game played on a 9x9 grid.
# (More info at: http://en.wikipedia.org/wiki/Sudoku)
# Sudoku Solution Validator for size N
# Write a function validSolution that accepts a 2D array representing a Sudoku board,
#  and returns true if it is a valid solution, or false otherwise.


import math
import numpy as np

COL_CODE = 0
ROW_CODE = 1

def target_sum(no_elements):
    # given the sum for a block, row, col:
    # is == sum(range(1,n))
    return (no_elements + 1 ) * (no_elements / 2.0)


def longest_axis(matrix):
        return max(matrix.shape)

def shortest_axis(matrix):
        return min(matrix.shape)


def _check_row_or_column(matrix, axiscode):
    """
    given a matrix, does its (row|col) add up correctly?
    :param matrix: a numpy matrux
    :param axiscode: COL_CODE | ROW_CODE
    :return: Boolean
    """
    try:
        target = get_sum_target(matrix)
        seq_sums = matrix.sum(axis=axiscode)
        seq_sums_correct = [s == target for s in np.nditer(seq_sums)]
        # lazy evaluation, so this isn't inefficient
        return all(seq_sums_correct)
    except TypeError:
        return False


def sudoku_grid_to_matrix(sudoku_grid):
    """
    convert a list of lists to a numpy matrix
    :param sudoku_grid: list (of lists)
    :return: numpy matrix
    """
    return np.matrix(sudoku_grid)

def get_sum_target(matrix):
    """
    Given a matrix what the target value for a block, row, or col?
    :param matrix: numpy matrix
    :return: int
    """
    longest = max(matrix.shape)
    target = target_sum(longest)
    return target

def check_rows(matrix):
    return _check_row_or_column(matrix, axiscode=ROW_CODE)

def check_columns(matrix):
    return _check_row_or_column(matrix, axiscode=COL_CODE)

def get_blockwidth(matrix):
    return int(math.sqrt(longest_axis(matrix)))

def sum_matrix(matrix):
    return matrix.sum()

def matrix_sum_correct(matrix, target):
    return sum_matrix(matrix) ==  target

def check_blocks(matrix):
    size = longest_axis(matrix)
    target = get_sum_target(matrix)
    step_size = get_blockwidth(matrix)
    for x in range(0,size,step_size):
        for y in range(0,size,step_size):
            submatrix = matrix[x:x + step_size, y:y + step_size]
            if target != sum_matrix(submatrix):
                return False
    return True


def is_matrix_square(matrix):
    return shortest_axis(matrix) == longest_axis(matrix)

def is_matrix_positive_numbers(matrix):
    try:
        return matrix.min()>0
    except TypeError:
        return False

def sides_count_is_square_number(matrix):
    return longest_axis(matrix) == math.pow(get_blockwidth(matrix), 2)

def check_matrix_elements_not_boolean(matrix):
    for x in np.nditer(matrix.flatten()):
        if str(x) in ( 'True', 'False'):
            return False
    return True


class Sudoku(object):

    def __init__(self, sudoku_grid):
        self.matrix = sudoku_grid_to_matrix(sudoku_grid)

    def is_valid(self):
        return sides_count_is_square_number(self.matrix) and \
               is_matrix_positive_numbers(self.matrix) and \
               is_matrix_square(self.matrix) and \
               check_matrix_elements_not_boolean(self.matrix) and \
               check_columns(self.matrix) and \
               check_rows(self.matrix) and \
               check_blocks(self.matrix)


import unittest
class TestFirst(unittest.TestCase):
    def testFirst(self):
        test = self
        Test = self
        test.assert_equals = Test.assertEqual
        Test.assert_equals = Test.assertEqual
        goodSudoku1 = Sudoku([
          [7,8,4, 1,5,9, 3,2,6],
          [5,3,9, 6,7,2, 8,4,1],
          [6,1,2, 4,3,8, 7,5,9],

          [9,2,8, 7,1,5, 4,6,3],
          [3,5,7, 8,4,6, 1,9,2],
          [4,6,1, 9,2,3, 5,8,7],

          [8,7,6, 3,9,4, 2,1,5],
          [2,4,3, 5,6,1, 9,7,8],
          [1,9,5, 2,8,7, 6,3,4]
        ])

        goodSudoku2 = Sudoku([
          [1,4, 2,3],
          [3,2, 4,1],

          [4,1, 3,2],
          [2,3, 1,4]
        ])

        # Invalid Sudoku
        badSudoku1 = Sudoku([
          [0,2,3, 4,5,6, 7,8,9],
          [1,2,3, 4,5,6, 7,8,9],
          [1,2,3, 4,5,6, 7,8,9],

          [1,2,3, 4,5,6, 7,8,9],
          [1,2,3, 4,5,6, 7,8,9],
          [1,2,3, 4,5,6, 7,8,9],

          [1,2,3, 4,5,6, 7,8,9],
          [1,2,3, 4,5,6, 7,8,9],
          [1,2,3, 4,5,6, 7,8,9]
        ])

        badSudoku2 = Sudoku([
          [1,2,3,4,5],
          [1,2,3,4],
          [1,2,3,4],
          [1]
        ])

        badSudoku3 = Sudoku([[True],])

        # Test.it('should be valid')
        Test.assert_equals(goodSudoku1.is_valid(), True, 'Testing valid 9x9')
        Test.assert_equals(goodSudoku2.is_valid(), True, 'Testing valid 4x4')

        # Test.it ('should be invalid')
        Test.assert_equals(badSudoku1.is_valid(), False, 'Values in wrong order')
        print badSudoku2.is_valid()
        Test.assert_equals(badSudoku2.is_valid(), False, '4x5 (invalid dimension)')
        Test.assert_equals(badSudoku3.is_valid(), False, 'true (invalid dimension)')