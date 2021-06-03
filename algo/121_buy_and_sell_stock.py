import unittest
from typing import List
from time import time, sleep

from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter

import numpy as np
import pandas as pd


# [1, 2] -> 1
# [7, 1, 5, 3, 6, 4] -> 5 for buying at day1 and selling at day4
# bf: O(N^2)
def max_profit_bf(prices: List[int]) -> int:
    n = len(prices)
    high = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if (prices[j] - prices[i]) > high:
                high = prices[j] - prices[i]

    return high

def max_profit(prices: List[int]) -> int:
    min_price = float('inf')
    high = 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif (prices[i] - min_price) > high:
            high = prices[i] - min_price
    return high
            
def main():
    # driver_code
    prices = [7,1,5,3,6,4]
    print(max_profit(prices))

if __name__ == '__main__':
    main()