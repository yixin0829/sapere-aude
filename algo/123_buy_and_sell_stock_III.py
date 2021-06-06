import unittest
from typing import List
from time import time, sleep

from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter

import numpy as np
import pandas as pd


# O(nlogn) solution with trackers and sorting
# bug: does not work since you only got 2 sells. you might NOT want to sell even you reach a peak but wait a bit longer
def sol(prices: List[int]) -> int:
    trsc = []
    n = len(prices)
    hold = 0
    
    for i in range(1, n):
        if prices[i] >= prices[i-1]:
            hold += prices[i] - prices[i-1]
        else:
            trsc.append(hold)
            hold = 0 # sell it

        # check if final sell (at the end)
        if i == (n-1) and hold:
            trsc.append(hold)

    # sum up for the top 2 O(nlogn)
    print(trsc)
    trsc.sort(reverse=True)
    print(trsc)
    return sum(trsc[0:2])

# attempt 2 -> bf: find all the peaks and valleys and do a O(n^2)
def sol2(prices: List[int]) -> int:
    hl = [] # high & low
    n = len(prices)
        

def main():
    # driver_code
    prices = [3,3,5,0,0,3,1,4]
    prices2 = [1,2,4,2,5,7,2,4,9,0] # buy 1 sell 7 + buy 2 sell 9 (note we forgo the option to sell at 4, a peak)
    print(sol2(prices))
    print(sol2(prices2))

if __name__ == '__main__':
    main()