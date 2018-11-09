# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None or root == p or root == q:
            return root
        lTree = self.lowestCommonAncestor(root.left, p, q)
        rTree = self.lowestCommonAncestor(root.right, p, q)
        if rTree and lTree:
            return root
        else:
            return lTree or rTree
