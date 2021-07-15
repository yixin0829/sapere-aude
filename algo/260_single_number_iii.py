import unittest
from typing import List
from time import time, sleep

from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter

import numpy as np
import pandas as pd


# sort it and one pass O(nlogn) time and O(1) space
# OR using bit manipulation - that should be the only way to archieve O(n) time and O(1) space

## O(n) time and O(n) space (87% faster)
def single_num_hash(nums: List[int]) -> List[int]:
    ans = []
    counter = {}
    for n in nums:
        if n not in counter:
            counter[n] = 1
        else:
            counter[n] += 1
        
    for n in list(counter.keys()):
        if counter[n] == 1:
            ans.append(n)
    
    return ans
    
# two-pass bit manipulation (for fun)
# https://leetcode.com/problems/single-number-iii/discuss/1338383/C%2B%2B-Bitwise-Solution-O(N)
def single_num_bit(nums: List[int]) -> List[int]:
    # total XOR of nums array
    txor = 0
    for n in nums:
        txor ^= n

    # get bit mask of right most set bit
    mask = 1
    while (txor & mask) == 0:
        mask = mask << 1

    a, b = 0, 0
    for n in nums:
        if (n&mask) == 0: a ^= n
        else: b ^= n
    
    return [a, b]


def main():
    # driver_code
    nums = [1,2,1,3,2,5]
    print(single_num_bit(nums))

if __name__ == '__main__':
    main()