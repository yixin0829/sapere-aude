import unittest
from typing import List
from time import time, sleep

from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter

import numpy as np
import pandas as pd

# ex
# digits = 2,3
# output = [ad, ae, af, bd, be, bf, cd, ce, cf]

# digits = 2,3,4
# output = [...]
    

# bf O(3^n) - exp time (but can use recursion to overcome the for loop issue)
def letterComb(digits: str) -> List[str]:
    # srp the string into a list of int
    l = [int(char) for char in digits] # l = [d for d in digits]
    mapping = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}
    # a_ord = ord('a')
    # for i in range(8):
    #     starting = a_ord + i*3
    #     mapping[i+1] = [chr(starting), chr(starting+1), chr(starting+2)]

    #     if i == 7:
    #         mapping[i+1] = [chr(starting), chr(starting+1), chr(starting+2), chr(starting+3)]
    # print(mapping)


    def helper(l):
        # basis - empty list
        if not l:
            return []

        num = l.pop() # default pop left
        ans = helper(l)
        new_ans = []
        if ans:
            for comb in ans:
                for c in mapping[num]:
                    new_ans.append(comb + c)
        else:
            new_ans = mapping[num]
        return new_ans

    return helper(l)


def main():
    # driver_code
    digits = "234"
    print(letterComb(digits))

if __name__ == '__main__':
    main()