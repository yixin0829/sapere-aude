import unittest
from typing import List
from time import time, sleep

from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter

import numpy as np
import pandas as pd


# backtracking approach O(2^n) complexity
def climb_bt(n: int) -> int:
    def bt(n: int, current: int):
        if current == n:
            return 1
        elif current > n:
            return 0
        
        s = bt(n, current+1) + bt(n, current+2)
        return s
    ans = bt(n, 0)
    
    return ans


# dynamic programming (memorization)
# O(n) time with O(n) space
def climb_dp_mem(n: int) -> int:
    mem = [0] * (n*3) # some extra space for slack
    def dp(n, current):
        if current == n:
            mem[current] = 1
            return 1
        elif current > n:
            return 0
        
        a = mem[current+1] if mem[current+1] != 0 else dp(n, current+1)
        b = mem[current+2] if mem[current+2] != 0 else dp(n, current+2)
        mem[current] = a + b

        return mem[current]
    ans = dp(n, 0)

    return ans
        
# official solution recursive dp with memorization (pruning the recusion tress with the help from memo)
def climb_dp_mem2(n: int) -> int:
    mem = [0] * (n+1) # preferred way to init 1d array in python
    def dp(n, current):
        if current == n:
            mem[current] = 1
            return 1
        elif current > n:
            return 0

        if mem[current]:
            return mem[current]
        
        mem[current] = dp(n, current+1) + dp(n, current+2)
        return mem[current]
    
    ans = dp(n, 0)

    return ans


# non-recursive dp O(n) time and O(n) space
def climb_dp_non_recur(n: int) -> int:
    if n < 1:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for cur in range(3, n+1):
        dp[cur] = dp[cur - 1] + dp[cur - 2]

    return dp[n]

# Fibonacci number: realize the prev dp problem is just a Fibonacci sequence
# O(n) time and O(1) space
def climb_fibonacci(n: int) -> int:
    if n == 1: return 1

    first = 1
    second = 2
    for i in range(3, n+1):
        third = first + second
        first = second
        second = thrid
    return second

def main():
    # driver_code
    print(climb(1))
    # 1, 1, 2
    # 2, 2
    # 1, 1, 1, 1
    # 2, 1, 1
    # 1, 2, 1

if __name__ == '__main__':
    main()