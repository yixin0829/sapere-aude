from typing import List
from time import time
# input array is sorted

# since it's sorted. perfect for two-ptr in O(n) time and O(1) space
def sol(nums: List[int], target: int) -> List[int]:
    l = 0
    r = len(nums) - 1

    while l < r:
        if target == (nums[l] + nums[r]):
            return [l+1, r+1]
        elif target < (nums[l] + nums[r]):
            r -= 1
        elif target > (nums[l] + nums[r]):
            l += 1

    return []

# note it's still slower than the one-pass hash lookback approach

def main():
    # driver_code
    nums = [2,7,11,15]
    tar = 9
    print(sol(nums, tar))

if __name__ == '__main__':
    main()