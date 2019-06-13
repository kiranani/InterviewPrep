# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        l = 1
        left, right = root.left, root.right
        while left and right:
            l += 1
            left, right = left.left, right.right
        if not left and not right:
            return 2 ** l - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
       
