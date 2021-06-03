import unittest
from typing import List
from time import time, sleep

from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter

import numpy as np
import pandas as pd


def max_profit(prices:List[int]) -> int:
    # buy at the valley and sell at the peak (buy low sell high)
    pass
    

def main():
    # driver_code
    prices = [7,1,5,3,6,4]
    print(max_profit(prices))

if __name__ == '__main__':
    main()