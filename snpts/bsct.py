from typing import List
from time import time
from bisect import bisect, bisect_left, bisect_right
import numpy as np
import pandas as pd


def main():
    # driver_code
    nums = [1, 2, 3, 3, 3, 5]
    nums_unsorted = [1, 5, 3, 2, 3, 3]
    tar1 = 4
    tar2 = 3
    print(f'insert {tar1} to the left-most possible idx in nums: ', end='')
    print(bisect_left(nums, tar1))
    print(f'insert {tar1} to the left-most possible idx in nums_unsorted: ', end='')
    print(bisect_left(nums_unsorted, tar1)) # * does NOT work on unsorted list

    print(f'insert {tar1} to the right-most possible idx in nums: ', end='')
    print(bisect_right(nums, tar1))
    print(f'insert {tar2} to the right-most possible idx in nums with lo=0 and hi=3: ', end='')
    print(bisect_right(nums, tar2, lo=0, hi=3))
    print(f'insert {tar2} to the right-most possible idx in nums: ', end='')
    print(bisect_right(nums, tar2))

if __name__ == '__main__':
    main()