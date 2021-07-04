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

# bug: in order approach not working - only check values but not structure
def is_sym(root: TreeNode) -> bool:
    # helper check if subtrees are the same
    result = []
    def inorder(root: TreeNode):
        # base
        if not root:
            return
        
        inorder(root.left)
        result.append(root.val) # "visit" the current node
        inorder(root.right)
    
    inorder(root)
    l, r = 0, len(result) -1
    palin = True
    while l < r:
        if result[l] != result [r]:
            palin = False
            break
        l += 1
        r -= 1
    
    return palin

## recursive approach: faster than 59%
def is_sym(root: TreeNode) -> bool:
    ans = True

    # check if subtree from root1 is the same as subtree from root2
    def helper(root1, root2):
        nonlocal ans #* important to have if wanna change outer variables in inner function
        if not root1 and not root2:
            return
        elif root1 and root2:
            if root1.val != root2.val:
                ans = False
                return

            helper(root1.left, root2.right) # outer check
            helper(root1.right, root2.left) # inner check
        else:
            ans = False
            return

    helper(root.left, root.right)
    return ans

## standard recursive approach with helper function returning bool: faster than 95%
# O(n) time and O(n) space for recursive call on the stack
def is_sym_recur2(root: TreeNode) -> bool:
    def helper(r1, r2) -> bool:
        if (not r1 and not r2): return True
        if (not r1 or not r2): return False
        return (r1.val == r1.val) and helper(r1.left, r2.right) and helper(r1.right, r2.left)

    return helper(root.left, root.right)

## iterative approach: use a queue O(n) time and O(n) space faster than 59%
def is_sym_iter(root: TreeNode) -> bool:
    if not root:
        return True

    dq = deque([(root.left,root.right),])
    while dq:
        node1, node2 = dq.popleft()
        if not node1 and not node2: # both are NULL
            continue
        if not node1 or not node2: # one of them are NULL
            return False
        if node1.val != node2.val:
            return False
        # node1.left and node2.right are symmetric nodes in structure
        # node1.right and node2.left are symmetric nodes in structure
        dq.append((node1.left,node2.right))
        dq.append((node1.right,node2.left))
    return True


def test():
    ans = True
    def invert():
        nonlocal ans
        ans = False
        return
    invert()
    return ans
    

def main():
    # driver_code
    print(test())

if __name__ == '__main__':
    main()