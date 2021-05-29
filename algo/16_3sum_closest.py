from typing import List
from time import time, sleep
from bisect import bisect, bisect_left, bisect_right

# return the sum of the three integers. may assume that each input would have exactly one solution
# for each ele compute new target and then use two pointer (need sorting first but in total O(n^2) so doesn't matter)
# bug: updating is broken for test case 3 (look at while loop)
def sol(nums: List[int], target: int) -> int:
    n = len(nums)

    if n == 3:
        return sum(nums)
    elif n < 3:
        return -1

    nums.sort() # in-place sort (return nothing)
    clst = []
    for i in range(len(nums) - 2):
        new_tar = target - nums[i]
        # only need to run two-ptr on the right part of the cur (can prove by contradiction)
        l = i+1
        r = n-1
        
        while l < (r-1):
            s = nums[l] + nums[r]
            # only move one ptr if it gets closer to the new_tar, else break
            if s < new_tar and abs(nums[l+1] + nums[r] - new_tar) <= abs(nums[l] + nums[r] - new_tar):
                l += 1
            elif s > new_tar and abs(nums[l] + nums[r-1] - new_tar) <= abs(nums[l] + nums[r] - new_tar):
                r -= 1
            elif s == new_tar:
                return target
            else:
                break

        clst.append(nums[i] + nums[l] + nums[r])
        
    f = lambda x: abs(x - target) # creating a shorthand lambda
    clst.sort(key=f) # sort using shallow list abs(x - target) in ASC order

    return clst[0]


# * official two-ptr solution (see how elegant it is!)
# space: O(logn) to O(n) depending on the sorting algo
# time: O(nlogn + n^2) = O(n^2)
def threeSumClosest(nums: List[int], target: int) -> int:
    diff = float('inf') # python3 trick
    nums.sort()

    # range - 2 since don't want l to be out-of-bound or overlapping with r
    for i in range(len(nums)-2):
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if abs(target - s) < abs(diff):
                diff = target - s
            if s < target:
                l += 1
            else:
                r -= 1
        if diff == 0:
            break

    return target - diff


# binary search approach: fix two and search for one (less efficient than 2-ptr)
def sol_bs(nums: List[int], target: int) -> int:
    diff = float('inf')
    nums.sort()
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            complement = target - nums[i] - nums[j]
            hi = bisect_right(nums, complement, j + 1)
            lo = hi - 1
            if hi < len(nums) and abs(complement - nums[hi]) < abs(diff):
                diff = complement - nums[hi]
            if lo > j and abs(complement - nums[lo]) < abs(diff):
                diff = complement - nums[lo]

        if diff == 0:
            break
    return target - diff


def main():
    # driver_code
    nums = [-1,2,1,-4]
    nums2 = [1,1,1,1]
    nums3 = [1,2,5,10,11]
    nums4 = [4,0,5,-5,3,3,0,-4,-5]
    tar = 1
    tar2 = 0
    tar3 = 12
    tar4 = -2
    print(sol_bs(nums, tar))
    print(sol_bs(nums2, tar2))
    print(sol_bs(nums3, tar3))
    print(sol_bs(nums4, tar4))

if __name__ == '__main__':
    main()