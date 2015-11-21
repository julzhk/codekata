# Sudoku is a game played on a 9x9 grid.
# The goal of the game is to fill all cells of the grid with digits from 1 to 9,
# so that each column, each row, and each of the nine 3x3 sub-grids
# (also known as blocks) contain all of the digits from 1 to 9.
# (More info at: http://en.wikipedia.org/wiki/Sudoku)

# Sudoku Solution Validator

# Write a function validSolution that accepts a 2D array representing a Sudoku board,
#  and returns true if it is a valid solution, or false otherwise.
# The cells of the sudoku board may also contain 0's,
# which will represent empty cells.
# Boards containing one or more zeroes are considered to be invalid solutions.

import numpy as np

COL_CODE = 0
ROW_CODE = 1
RETURN_MSG_INCORRECT = 'Try again!'
RETURN_MSG_CORRECT = 'Finished!'

def target_sum(no_elements):
    # given the sum for a block, row, col:
    # is == sum(range(1,n))
    return (no_elements + 1 ) * (no_elements / 2.0)


def longest_axis(matrix):
        # sudoku should be square though!
        return max(matrix.shape)


def _check_row_or_column(matrix, axiscode):
    """
    given a matrix, does its (row|col) add up correctly?
    :param matrix: a numpy matrux
    :param axiscode: COL_CODE | ROW_CODE
    :return: Boolean
    """
    target = get_sum_target(matrix)
    seq_sums = matrix.sum(axis=axiscode)
    seq_sums_correct = [s == target for s in np.nditer(seq_sums)]
    # lazy evaluation, so this isn't inefficient
    return all(seq_sums_correct)


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
    # 3 blocks vertical and horizontally
    return longest_axis(matrix) / 3

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

def done_or_not(sudoku_grid):
    matrix = sudoku_grid_to_matrix(sudoku_grid)
    done = check_columns(matrix) and check_rows(matrix) and check_blocks(matrix)
    return RETURN_MSG_CORRECT if done else RETURN_MSG_INCORRECT


import unittest
class TestFirst(unittest.TestCase):
    def testFirst(self):
        test = self
        Test = self
        test.assert_equals = Test.assertEqual
        Test.assert_equals = Test.assertEqual

        Test.assert_equals(target_sum(2),3)
        Test.assert_equals(target_sum(3),6)
        Test.assert_equals(target_sum(4),10)
        Test.assert_equals(target_sum(5),15)
        Test.assert_equals(target_sum(6),21)

        Test.assert_equals(longest_axis(np.matrix([[1,2],[2,3],[3,4]])),3)
        Test.assert_equals(longest_axis(np.matrix([[1,2]])),2)
        Test.assert_equals(check_rows(sudoku_grid_to_matrix([[1,2],[2,1]])), True)
        Test.assert_equals(check_rows(sudoku_grid_to_matrix([[1,2,4]])), False)
        Test.assert_equals(check_rows(sudoku_grid_to_matrix([[1,2,3,4,5,6,7,8,9]])), True)
        Test.assert_equals(check_rows(sudoku_grid_to_matrix([1,2,3,4,5,6,7,8,8])), False)

        Test.assert_equals(check_columns(sudoku_grid_to_matrix([[1,2],[2,1]])), True)
        Test.assert_equals(check_columns(sudoku_grid_to_matrix([[1,2],[2,2]])), False)
        Test.assert_equals(check_columns(sudoku_grid_to_matrix([[2,2],[2,1]])), False)
        Test.assert_equals(check_columns(sudoku_grid_to_matrix([[1,2],[2,1]])), True)
        Test.assert_equals(check_columns(sudoku_grid_to_matrix([[1,2,3],[4,5,6],[7,8,8]])), False)
        Test.assert_equals(check_columns(sudoku_grid_to_matrix([[2,2,2],[2,2,2],[2,2,2]])), True)
        Test.assert_equals(check_columns(sudoku_grid_to_matrix([[2,2,2],[2,2,2],[2,2,3]])), False)
        Test.assert_equals(check_columns(sudoku_grid_to_matrix([[2,2,1],[2,2,2],[2,2,3]])), True)
        Test.assert_equals(check_blocks(sudoku_grid_to_matrix([[6,6,6],[6,6,6],[6,6,6]])),True)