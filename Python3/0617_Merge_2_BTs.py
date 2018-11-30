# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        def recurse(r1, r2):
            if r1 is not None and r2 is not None:
                r1.val += r2.val
                r1.left = recurse(r1.left, r2.left)
                r1.right = recurse(r1.right, r2.right)
                return r1
            elif r1 is None:
                return r2
            else:
                return r1
        return recurse(t1, t2)
        
