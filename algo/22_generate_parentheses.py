import unittest
from typing import List
from time import time, sleep

from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter

import numpy as np
import pandas as pd

#* need more practice

# example: n=2
# ['()()', '(())', '(())']

# bf: O(2^(2n)n) time, and O(2^(2n)) space
# pass

# backtracking
# left - open (
# right - close )
def gen(n: int) -> List[str]:
    ans = []
    def backtrack(s = [], left = 0, right = 0):
        # base case
        if len(s) == 2 * n:
            ans.append(''.join(s))
            return

        if left < n:
            s.append('(')
            backtrack(s, left+1, right)
            s.pop()
        if right < left: # close cannot exceed open
            s.append(')')
            backtrack(s, left, right+1)
            s.pop()

    backtrack()
    return ans

def main():
    # driver_code
    n = 4
    print(gen(4))

if __name__ == '__main__':
    main()