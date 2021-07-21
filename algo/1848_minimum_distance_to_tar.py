import unittest
from typing import List
from time import time, sleep

from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter

import numpy as np
import pandas as pd


# like a simplified version of BFS in graph formulation (path finding in 1d)
# use two-ptr technique
def get_min_dist(nums: List[int], target: int, start: int) -> int:
    if nums[start] == target:
        return 0

    left = start - 1
    right = start + 1
    while True:
        if left >= 0 and nums[left] == target:
            return (start - left)
        if right < len(nums) and nums[right] == target:
            return (right - start)
        left -=1
        right += 1




def main():
    # driver_code
    nums = [5,3,6]
    target = 5
    start = 2
    print(get_min_dist(nums, target, start))

if __name__ == '__main__':
    main()