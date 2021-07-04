import unittest
from typing import List
from time import time, sleep
import math

from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter

import numpy as np
import pandas as pd

# my sol: not working (top-down validation in O(n) time)
def validate(root: TreeNode) -> bool:
    ans = True
    def helper(cur: TreeNode):
        nonlocal ans
        if not ans or not cur: # base
            return

        if cur.left and not cur.right:
            # case 1: only left
            if cur.left.val < cur.val:
                helper(cur.left)
            else:
                ans = False
                return
        elif not cur.left and cur.right:
            # case 2: only right
            if cur.val < cur.right.val:
                helper(cur.right)
            else:
                ans = False
                return
        elif cur.left and cur.right:
            # case 3: complete
            if cur.left.val < cur.val and cur.val < cur.right.val:
                helper(cur.left)
                helper(cur.right)
            else:
                ans = False
                return
        else:
            # case 4: leaf
            return

    helper(root)
    return ans
        
# 9.72% faster (vanilla recusive) O(n) time and O(1) space
def validate(root: TreeNode) -> bool:
    ans = True
    def helper(cur: TreeNode, min, max) -> bool:
        if not cur:
            return True # base case

        if cur.val <= min or cur.val >= max:
            return False
        
        return helper(cur.left, min, cur.val) and helper(cur.right, cur.val, max)
    
    return helper(root, -math.inf, math.inf)

## same method as above but 96% faster
def validate(root: TreeNode) -> bool:
    result = True
    def helper(root, left, right):
        nonlocal result #* important: basically telling python that result is not a local variable in inner function. without this declaration we cannot change `result` in the recursive calls
        if(root):
            if(left >= root.val or root.val >= right):
                result = False
                return
            helper(root.left, left, root.val)
            helper(root.right, root.val, right)
    helper(root, float("-inf"), float('inf'))
    return result

## approach 2: in-order traversal bst will print out tree "in-order" (iterative approach) 71% faster
def validate(root: TreeNode) -> bool:
    pre, cur, stack = None, root, []
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        s = stack.pop()
        if pre and s.val <= pre.val: # compare with the previous node (in-order property)
            return False
        pre, cur = s, s.right
    return True

def main():
    # driver_code
    pass

if __name__ == '__main__':
    main()