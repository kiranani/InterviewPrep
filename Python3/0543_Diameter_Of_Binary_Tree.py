# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def helper(root, m):
            if root is None:
                return 0, 0
            l, r = helper(root.left, m), helper(root.right, m)
            p = l[0] + r[0] if l[0] + r[0] > 0 else 0
            m = p if p > m else m
            return 1 + max(l[0], r[0]), max(m, l[1], r[1])
        return helper(root, 0)[1]
        
