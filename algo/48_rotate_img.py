import unittest
from typing import List
from time import time, sleep

from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter

import numpy as np
import pandas as pd

# * same as ctci chapter 1 rotate matrix
def sol():
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
