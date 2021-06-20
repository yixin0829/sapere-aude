# O(MxN)
import unittest
from copy import deepcopy
## redo

# 1st attempt: bf approach (not in place but passed leetcode)
def zero_matrix_1(matrix):
    # testing PAT (personal access token)
    # testing PAT attempt 2
    rows = len(matrix)
    cols = len(matrix[0])

    # init a new matrix as flagging
    nm = [[1 for i in range(cols)] for j in range(rows)]

    # traverse and flag O(n^3)
    for row in range(rows):
        for col in range(cols):
            ele = matrix[row][col]
            if not ele:
                # row to zeros
                nm[row] = [0] * cols
                # col to zeros
                for i in range(rows):
                    nm[i][col] = 0
    
    # set input matrix 0 entries
    for row in range(rows):
        for col in range(cols):
            if nm[row][col] == 0:
                matrix[row][col] = 0

    return matrix

# not in place attempt
def zero_matrix_2(matrix):
    m = len(matrix)
    n = len(matrix[0])
    rows = set()
    cols = set()

    for x in range(m):
        for y in range(n):
            if matrix[x][y] == 0:
                rows.add(x)
                cols.add(y)

    for x in range(m):
        for y in range(n):
            if (x in rows) or (y in cols):
                matrix[x][y] = 0

    return matrix


# in-place
def zero_matrix_ip(matrix):
    pass

def zero_matrix_pythonic(matrix):
    pass


class Test(unittest.TestCase):

    test_cases = [
        (
            [
                [1, 2, 3, 4, 0],
                [6, 0, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 0, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [11, 0, 13, 14, 0],
                [0, 0, 0, 0, 0],
                [21, 0, 23, 24, 0],
            ],
        )
    ]
    # testable_functions = [zero_matrix, zero_matrix_pythonic]
    testable_functions = [zero_matrix]

    def test_zero_matrix(self):
        for f in self.testable_functions:
            for [test_matrix, expected] in self.test_cases:
                test_matrix = deepcopy(test_matrix)
                assert f(test_matrix) == expected


if __name__ == "__main__":
    unittest.main()
