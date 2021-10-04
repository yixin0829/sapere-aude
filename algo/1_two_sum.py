from typing import List

# Better comments
## note
#* highlight
# question:...
# bug:...
#// strikethrough

# hash table one-pass approach - O(n) time
def two_sum(nums: List[int], target: int) -> List[int]:
    d = {} # val : idx in nums
    for i, n in enumerate(nums):
        cpm = target - n
        # look for cpm in the
        if cpm in d:
            return [d[cpm], i]
        else:
            d[n] = i

    return [] # DNE

# two-ptr technique on sorted array - O(nlogn) time (two pass) - pretty slow
def two_sum_tp(nums: List[int], target: int) -> List[int]:
    # since after sorting the idx will change. the 1st pass will mapp element i
    # to a list of idx (in case duplication in the given nums)

    # 1st pass
    d = {}
    for i, n in enumerate(nums):
        if n in d:
            d[n].append(i)
        else:
            d[n] = [i]

    nums.sort() # then sort arr O(nlogn)
    l = 0
    r = len(nums) - 1

    # 2nd pass (two ptr) - O(logn)
    while l < r:
        s = nums[l] + nums[r]
        if s == target:
            # note we map back to original indices
            l_map = d[nums[l]][0]
            if nums[l] == nums[r]:
                r_map = d[nums[r]][1] # e.g. [3, 3] tar = 6
            else:
                r_map = d[nums[r]][0]
            return [l_map, r_map]
        elif s < target:
            l += 1
        elif s > target:
            r -= 1
    
    return []

def main():
    test1 = [2, 11, 7, 15]
    test2 = [3, 2, 4]
    tar1 = 9
    tar2 = 6
    print(two_sum_tp(test2, tar2))

if __name__ == '__main__':
    main()