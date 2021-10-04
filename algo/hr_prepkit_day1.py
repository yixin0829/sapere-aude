#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    cnt = [0] * 3
    for num in arr:
        if num < 0: # neg
            cnt[0] += 1
        elif num == 0: # zeros
            cnt[1] += 1
        else: # pos
            cnt[2] += 1
    
    n = len(arr)
    print(round(cnt[2]/n, 6)) # fraction of pos
    print(round(cnt[0]/n, 6)) # fraction of neg
    print(round(cnt[1]/n, 6)) # fraction of zeros

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    # initialize trackers
    max_, min_ = 0, float('inf')
    
    # sum arr
    s = sum(arr)
    
    # loop through each num in arr
    for num in arr:
        ss = s - num # sum of 4 out of 5 integers
        
        # minus the num from the sum and update max_, min_
        max_ = max(ss, max_)
        min_ = min(ss, min_)
    
    print(f'{min_} {max_}')

#
# Mock: Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s: str) -> str:
    # Write your code here
    
    # parse if it's PM or AM
    hour = int(s[:2])
    if s[-2:] == 'PM': # if PM
        # if 1PM - 11:59PM need to add 12 to the hours
        if hour != 12:
            return f'{hour + 12}{s[2:-2]}'
        else: # 12PM - 12:59PM no change needed
            return f'{s[:-2]}'
    else: # if AM
        # 12AM- 12:59AM need to minus 12 from the hours
        if hour == 12:
            return f'00{s[2:-2]}' #* be careful
        else: # 1AM - 11:59AM no change needed
            return f'{s[:-2]}'
    

# Mock: implement a funciton to find median of an unsorted array with odd length
def findMed(arr) -> int:
    arr.sort()
    mid = len(arr) // 2
    return arr[mid]