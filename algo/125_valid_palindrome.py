import unittest
from typing import List
from time import time, sleep
import re

from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter

import numpy as np
import pandas as pd


## method1 (fastest time-wise): compare with the reversed string
def is_plain(s: str) -> bool:
    # strip everything but alphanumberic char in the given string
    s = re.sub(r'\W+|_', '', s.lower())

    return s == s[::-1]

# method2: same as above but use reversed() built-in function
def is_plain2(s: str) -> bool:
    # strip everything but alphanumberic char in the given string
    s = re.sub(r'\W+|_', '', s.lower())

    rev_s = ''.join(reversed(s))
    return s == rev_s

# method3: iterative way (tail and head)
def is_plain3(s: str) -> bool:
    # strip everything but alphanumberic char in the given string
    s = re.sub(r'\W+|_', '', s.lower())

    left = 0
    right = len(s) - 1
    while left <= right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False

    return True

def main():
    # driver_code
    pass

if __name__ == '__main__':
    main()