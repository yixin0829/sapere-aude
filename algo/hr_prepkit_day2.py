#!/bin/python3

import math
import os
import random
import re
import sys

#
# *Complete the 'lonelyinteger' function below. (Lovely question)
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a) -> int:
    # Write your code here
    uniq_sum = sum(set(a))
    # lonely number will will uniq * 2 -  sum(a)
    lonely = uniq_sum * 2 - sum(a)
    return lonely


#
# *Complete the 'diagonalDifference' function below. (Lovely question)
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr) -> int:
    # Write your code here
    
    n = len(arr) # dimension of the SQUARE matrix
    
    # loop with two iterators
    # calculate right to left diagonal
    s1 = 0
    for i, j in zip(range(n), reversed(range(n))):
        s1 += arr[i][j]
        
    # calculate left to right diagonal
    s2 = 0
    for i, j in zip(range(n), range(n)):
        s2 += arr[i][j]
        
    return abs(s1 - s2)


#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    # input: List[int]
    # output: List[int] with length 100
    
    # fastest way to initialize 1D array
    counter = [0] * 100
    
    for num in arr:
        counter[num] += 1
        
    return counte


#
# *Mock: Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

# time: O(N)
def flippingMatrix(matrix):
    # Write your code here
    n = len(matrix)
    s = 0
    for i in range(n//2):
        for j in range(n//2):
            s += max(matrix[i][j], matrix[i][n-j-1], matrix[n-i-1][j], matrix[n-i-1][n-j-1]) # O(1)
    return s