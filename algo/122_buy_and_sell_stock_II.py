import unittest
from typing import List
from time import time, sleep

from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter

import numpy as np
import pandas as pd


# my solution! O(2N) time O(1) space beat 16.3%
def max_profit(prices:List[int]) -> int:
    n = len(prices)
    if n == 1:
        return 0

    # buy at the valley and sell at the peak (buy low sell high)
    v = 0
    p = 0
    hold = 0
    profit = 0
    for i in range(0, len(prices)):
        if i == (n - 1):
            if prices[i] < prices[i-1]:
                break
            else:
                profit += (prices[i] - prices[v]) if hold else 0
                break
        elif i == 0 and prices[i] < prices[i+1]: # hold
            hold = 1
        
        if prices[i-1] >= prices[i] and prices[i+1] > prices[i]:
            hold = 1
            v = i

        if prices[i-1] < prices[i] and prices[i+1] <= prices[i]:
            hold = 0
            p = i
            profit += prices[p] - prices[v]
    
    return profit

# 2nd attempt: optimized O(n) beat 41%
def max_profit_op(prices: List[int]) -> int:
    n = len(prices)
    v = 0
    hold = 0
    profit = 0
    for i in range(n-1):
        if prices[i] < prices[i+1] and not hold: # up
            v = i
            hold = 1
        elif prices[i] > prices[i+1] and hold: # peak
            profit += prices[i] - prices[v]
            hold = 0
    
    if prices[n-1] >= prices[n-2] and hold:
        profit += prices[n-1] - prices[v]

    return profit
        

# fastest simple one pass: adding as long as the 2nd num is higher that the prev one
# (we will sum up all diffs eventually)
def max_profit_best(prices: List[int]) -> int:
    n = len(prices)
    if n == 1:
        return 0
    profit = 0
    for i in range(1, n):
        if prices[i] > prices[i-1]:
            # add the difference to profit!
            profit += prices[i] - prices[i-1]
    return profit
    

def main():
    # driver_code
    prices = [7,1,5,3,6,4] # ans: 7
    prices2 =[1,2,3,4,5] # ans: 4
    prices3 =[7,6,4,3,1] # ans: 0
    prices4 =[2,1,2,1,0,0,1] # flat line ans: 2
    prices5 =[5,2,3,2,6,6,2,9,1,0,7,4,5,0] # ans: 20
    print(max_profit_best(prices))
    print(max_profit_best(prices2))
    print(max_profit_best(prices3))
    print(max_profit_best(prices4))
    print(max_profit_best(prices5))

if __name__ == '__main__':
    main()