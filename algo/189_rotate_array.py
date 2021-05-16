from typing import List

# solution 2: cyclic replacement with O(n) time and O(1) constant space
def rotate_c(nums: List[int], k: int) -> None:
    # [1, 2, 3], k=2 -----> [2, 3, 1]
    n = len(nums)
    k %= n # avoid extra rotation if k is large

    start = count = 0
    while count < n:
        cur, prev = start, nums[start]
        while True:
            nxt_idx = (cur + k) % n
            # python built-in swapping method (without tmp)
            nums[nxt_idx], prev = prev, nums[nxt_idx]
            cur = nxt_idx
            count += 1 # one replacement

            if start == cur:
                break
        start += 1

# optimal: using a simple observation O(n) time with O(n) space (fastest)
def rotate_r(nums: List[int], k: int) -> None:
    n = len(nums)
    k %= n
    
    # since the roatation puts first (n-k) elements to the front IN-ORDER
    # we just need to slice and re-arrange (note: list[:] returns a shallow
    # copy of the orginal nums)
    nums[:] = nums[n-k:] + nums[:n-k]

def main():
    nums = [1, 2, 3]
    k = 2
    rotate_r(nums, k)
    print(nums)

if __name__ == '__main__':
    main()
    