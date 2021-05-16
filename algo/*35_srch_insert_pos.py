from typing import List

# note: binary search in sorted arrays
# sorted. use binary search with O(log n) runtime complexity
def srch_insert(nums:List[int], tar: int) -> int:
    n = len(nums)

    return bs(0, n-1, nums, tar)

# bug: return m in each scope in recursion (use bi-sect?)
def bs(l, r, nums, tar) -> int:
    if l > r:
        return l

    m = (l + r) // 2
    print(f'mid: {m} ({nums[m]})')
    if nums[m] < tar:
        bs(l+1, r, nums, tar)
    elif tar < nums[m]:
        bs(0, l-1, nums, tar)
        
    # if tar is the middle ele. return
    print(f'bs: returning... {m}')
    return m

def main():
    nums = [1,3,5,6,7,8]
    tar = 8
    print(srch_insert(nums, tar))

if __name__ == '__main__':
    main()
