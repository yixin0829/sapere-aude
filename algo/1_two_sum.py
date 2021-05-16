from typing import List

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

def main():
    input = [2, 7, 11, 15]
    tar = 9
    print(two_sum(input, tar))

if __name__ == '__main__':
    main()