# O(NxN)
import unittest
from copy import deepcopy


def rotate_matrix(matrix):
    """rotates a matrix 90 degrees clockwise (in-place)"""
    # left to bottom 0,4 -> 4,4
    n = len(matrix[0])

    for layer in range(n // 2):
        # define the frame
        right = n-1 - layer
        bottom = n-1 - layer
        left, top = layer, layer

        # i count up and j count down
        for i, j in zip(range(left, right), range(right, left, -1)):
            # right to bottom
            temp, matrix[bottom][i] = matrix[bottom][i], matrix[j][right]
            # bottom to left
            temp, matrix[i][left] = matrix[i][left], temp
            # left to top
            temp, matrix[top][j] = matrix[top][j], temp
            # top to right
            matrix[j][right] = temp

    return matrix
    

def rotate_matrix_pythonic(matrix):
    """rotates a matrix 90 degrees clockwise (cheated not in-place)"""
    n = len(matrix)
    result = [[0] * n for i in range(n)]  # empty list of 0s
    for i, j in zip(range(n), range(n - 1, -1, -1)):  # i counts up, j counts down
        for k in range(n):
            result[k][i] = matrix[j][k]

    return result


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