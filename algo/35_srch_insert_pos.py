from typing import List
from bisect import bisect_right, bisect_left, bisect

# # binary insertion search on sorted list
# * iterative approach: sorted. use binary search with O(log n) runtime complexity
def srch_insert(nums:List[int], target: int) -> int:
    n = len(nums)
    l = 0
    r = n-1

    while l < r:
        # iteratively narrowing the scope by hald each iter
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1 # search right half (exclusive)
        else:
            r = mid # search left including the mid
    
    if nums[l] == target:
        return l
    elif nums[l] > target:
        return l # insert idx (realize always will be larger then non-exist element)
    else:
        return l + 1

# * recursive approach log(n) time (but faster than iterative approach)
def srch_insert_r(nums:List[int], target: int) -> int:
    ret = bs(nums, 0, len(nums) - 1, target)
    if nums[ret] == target:
        return ret
    elif nums[ret] > target:
        return ret # insert idx (realize always will be larger then non-exist element)
    else:
        return ret + 1

# recusive helper
def bs(nums, l, r, target) -> int:
    # base case (instead returning -1 we will do sth different)
    if l >= r:
        return l

    mid = (l + r) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return bs(nums, l, mid - 1, target)
    else:
        return bs(nums, mid + 1, r, target)

# * built-in bisect() approach (suprisingly slower)
def bsct(nums:List[int], target: int) -> int:
    return bisect_left(nums, target)
    
def main():
    nums = [1,3,5,6]
    target = [1, 3, 6, 5, 2, 7, 0]
    ans = [0, 1, 3, 2, 1, 4, 0]

    for i, t in enumerate(target):
        if bsct(nums, t) == ans[i]:
            print(f'passed case{i}')
        else:
            print((f'failed case{i}. return{bsct(nums, t)} but expect {ans[i]}'))

if __name__ == '__main__':
    main()
