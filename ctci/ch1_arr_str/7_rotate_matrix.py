# O(NxN)
import unittest
from copy import deepcopy


def rotate_matrix(matrix):
    """rotates a matrix 90 degrees clockwise"""
    # left to bottom 0,4 -> 4,4
    n = len(matrix[0])
    if n % 2: # odd matrix layer 1, 3, 5, ...
        layers = n // 2 + 1
        l = 0
        while l < layers:
            # rotate a "hollow"  square
            dim = 2 * l + 1
            matrix[]



def rotate_matrix_pythonic(matrix):
    """rotates a matrix 90 degrees clockwise"""
    pass


class Test(unittest.TestCase):

    test_cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        (
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5],
            ],
        ),
    ]
    testable_functions = [rotate_matrix_pythonic, rotate_matrix]

    def test_rotate_matrix(self):
        for f in self.testable_functions:
            for [test_matrix, expected] in self.test_cases:
                test_matrix = deepcopy(test_matrix)
                assert f(test_matrix) == expected


if __name__ == "__main__":
    unittest.main()