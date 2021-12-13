import unittest
from typing import List
from time import time, sleep

from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter

import numpy as np
import pandas as pd

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# example: nums = [2, 2, 1] ----> output: 1

# example: [1, 2, 3, 1, 3] -> [1, 1, 2, 3, 3]
# O(1) space constraint

## mysol (sorting): sort and then loop from the begining O(nlogn) time and O(1) space assuming we use a constant-space sorting algorithm (e.g. heapsort)
def single_num_sort(nums: List[int]) -> int:
    nums.sort() # be careful to NOT use sorted() to return a new copy. sort it IN-PLACE for O(1) space
    for n in range(1, len(nums),2):
        if nums[n-1] != nums[n]:
            return nums[n-1]
    return nums[-1]


# hash table: O(n) time and O(n) space two-pass solution with hash table
def single_num_hash(nums: List[int]) -> int:
    s={}
    for i in nums:
        if i not in s:
            s[i]=1
        else:
            s[i]+=1
    for i in list(s.keys()):
        if s[i]==1:
            return i

## math: 2* (a + b + c) - (a + a + b + c + c) = b  !!!!!! 99.55% faster !!!!! O(2n) space and O(2n) time
def single_num_math(nums: List[int]) -> int:
    distinct = list(set(nums)) # get rid of duplicates

    return sum(distinct) * 2 - sum(nums)


## show-off: O(n) and  O(1) space bit manipulation with XOR, we can XOR all bits together to find the unique number.
def single_num_bit(nums: List[int]) -> int:
    a = 0
    for n in nums:
        a ^= n
    return a
    


def main():
    # driver_code
    nums = [4, 1, 2, 1, 2]
    print(single_num_math(nums))

if __name__ == '__main__':
    main()