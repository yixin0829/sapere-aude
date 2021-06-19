# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursive approach
def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0
    else:
        l = maxDepth(root.left) + 1
        r = maxDepth(root.right) + 1
        return max(l, r)