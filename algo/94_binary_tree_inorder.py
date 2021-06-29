import unittest
from typing import List
from time import time, sleep

from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter

import numpy as np
import pandas as pd

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(root: TreeNode) -> List[int]:
    ans = []
    def rec(root: TreeNode):
        if not root:
            return

        rec(root.left)
        ans.append(root.val)
        rec(root.right)
        return ans
        
    return rec(root)

def main():
    # driver_code
    pass

if __name__ == '__main__':
    main()