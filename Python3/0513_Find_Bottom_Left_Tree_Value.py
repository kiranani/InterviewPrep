# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = [-1, float("inf")]
        def recurse(node, level):
            if node:
                if level > ans[0]:
                    ans[0], ans[1] = level, node.val
                recurse(node.left, level + 1)
                recurse(node.right, level + 1)
        recurse(root, 0)
        return ans[1]
        
