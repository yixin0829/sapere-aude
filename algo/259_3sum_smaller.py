# https://www.geeksforgeeks.org/print-triplets-with-sum-less-than-or-equal-to-k/
from typing import List
from time import time, sleep
from bisect import bisect, bisect_left, bisect_right
import numpy as np
import pandas as pd


# Given an array of distinct integers and a sum value. Print all triplets with sum smaller than given sum value. Expected Time Complexity is O(n2).

# time: O(n^3)   space: O(1)
def sol_bf():
    pass

# two-ptr time: O(n^2)
def sol(nums:List[int], target:int) -> List[tuple]:
    n = len(nums)
    nums.sort()
    ans = []

    for i in range(n - 2):
        # run 2-ptr while fixing nums[i]
        l = i+1
        h = n-1
        while l < h:
            s = nums[i] + nums[l] + nums[h]
            if s >= target:
                h -= 1
            else:
                ## important - if sum is smaller than tar than means there're total (h - l) triplets satifying
                for x in range(l + 1, h + 1):
                    ans.append((nums[i], nums[l], nums[x]))
                l += 1
    return ans

def main():
    # driver_code
    # test 1
    nums = [1,2,-1,3]
    tar = 3
    ans = [(1,2,-1)] # 1 + 2 - 1 = 2 < 3
    print(sol(nums, tar))

    # test 2
    nums2 = [5,1,3,4,7]
    tar2 = 12
    ans = [(1,3,4), (1,3,5), (1,3,7), (1,4,5)]
    print(sol(nums2, tar2))

if __name__ == '__main__':
    main()