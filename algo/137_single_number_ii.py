import unittest
from typing import List
from time import time, sleep

from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter

import numpy as np
import pandas as pd


## FAstest: math approach. O(n) time and O(n) space 3 * (a + b) - (a + a + b + a) = 2b -> 2b/ 2 = b
def single_num_math(nums: List[int]) -> int:
    no_dup = list(set(nums))
    return ((sum(no_dup) * 3) - sum(nums)) // 2
    


def main():
    # driver_code
    pass

if __name__ == '__main__':
    main()