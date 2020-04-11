# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        d = [0]
        def traverse(node):
            if not node:
                return 0
            left, right = traverse(node.left), traverse(node.right)
            d[0] = max(d[0], left + right)
            return 1 + max(left, right)
        traverse(root)
        return d[0]
        
