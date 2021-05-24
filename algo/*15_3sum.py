from typing import List
from collections import Counter
from time import time

# timeout approach: for each element n perform two-sum algo with tar = -n
# bug: my sol. same approach as sol_2 but much slower (how to avoid duplicate triplets faster)
def sol(nums: List[int]) -> List[List[int]]:
    ans = []
    nums.sort()
    for i, a in enumerate(nums):
        # skip if already searched
        if a == nums[i - 1]:
            continue

        # let's use -n as the target (a + b + n = 0 -> a + b = -n)
        d = {} # num: count

        for j, b in enumerate(nums[i+1:]):
            # compute the complement
            comp = -a - b
            if comp in d:
                candi = [a, b, comp]
                # check make sure no duplicate triplets
                valid = True
                for tri in ans:
                    if Counter(tri) == Counter(candi):
                        # duplicate unordered triplets (skip)
                        valid = False
                        break
                
                if valid:
                    ans.append(candi)

            if b not in d:
                d[b] = 1
        
    return ans

# for each element run one-pass two-sum with different target O(n^2) time and O(n) worst space
def sol_2(nums: List[int]) -> List[List[int]]:
    # len <= 3 cases
    if len(nums) == 3 and sum(nums) == 0:
        return [nums]
    if len(nums) < 4:
        return []
    
    nums.sort()
    
    results = []
    
    for i in range(len(nums)-2):
        # run 2 sum on the rest of the list where -i is the target
        # dictionary method
        if nums[i] != nums[i-1] or i == 0:
            
            seenDict = {}
            target = -nums[i]

            for j in nums[i+1:]:
                if j in seenDict:
                    if seenDict[j] == 1:
                        results.append([nums[i], target - j, j])
                        seenDict[j] = 0
                        
                else:
                    seenDict[target-j] = 1
        
    return results
    

def main():
    nums = [-1,0,1,2,-1,-4]
    nums2 = []
    nums3 = [0]
    nums4 = [13,4,-6,-7,-15,-1,0,-1,0,-12,-12,9,3,-14,-2,-5,-6,7,8,2,-4,6,-5,-10,-4,-9,-14,-14,12,-13,-7,3,7,2,11,7,9,-4,13,-6,-1,-14,-12,9,9,-6,-11,10,-14,13,-2,-11,-4,8,-6,0,7,-12,1,4,12,9,14,-4,-3,11,10,-9,-8,8,0,-1,1,3,-15,-12,4,12,13,6,10,-4,10,13,12,12,-2,4,7,7,-15,-4,1,-15,8,5,3,3,11,2,-11,-12,-14,5,-1,9,0,-12,6,-1,1,1,2,-3]
    nums5 = [0,-6,0,-14,2,0,-9,5,-9,-8,-7,12,-4,14,-6,6,0,5,-2,6,-7,1,10,-10,-5,3,-2,-3,-13,-6,1,-6,3,9,-5,12,-6,-7,2,0,1,11,-11,4,2,-2,-5,-13,11,0,9,11,-13,-4,-13,-11,14,-8,1,8,1,9,-13,-11,3,-11,9,12,-2,-4,-11,6,14,-7,-5,1,-1,-3,-4,-5,12,12,13,6,-7,-15,10,14,14,-12,8,0,13,2,-3,1,-1,-9,-9,12,-6,-5,-5,-6,4,5,2,10,-13,13,12,6]
    print(sol(nums))
    print(sol(nums2))
    print(sol(nums3))

    start = time()
    print(len(sol(nums4)))
    end = time()
    print(f'sol time: {end - start:.4f}')

    start = time()
    print(len(sol_2(nums4)))
    end = time()
    print(f'sol2 time: {end - start:.4f}')

if __name__ == '__main__':
    main()