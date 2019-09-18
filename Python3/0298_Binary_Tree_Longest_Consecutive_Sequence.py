# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        m = 0
        def helper(root):
            if not root:
                return 0
            ln = helper(root.left)
            rn = helper(root.right)
            c = 1
            if ln and root.val == root.left.val - 1:
                c += ln
            if rn and root.val == root.right.val - 1:
                c = max(c, 1 + rn)
            nonlocal m
            m = max(m, c)
            return c
        helper(root)
        return m
        
