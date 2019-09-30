# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        m = 0
        def dfs(root):
            if not root:
                return 0
            lp, rp = 0, 0
            if root.left:
                p = dfs(root.left)
                if root.val == root.left.val:
                    lp = 1 + p
            if root.right:
                p = dfs(root.right)
                if root.val == root.right.val:
                    rp = 1 + p
            nonlocal m
            m = max(m, lp + rp)
            return max(lp, rp)
        dfs(root)
        return m
        
