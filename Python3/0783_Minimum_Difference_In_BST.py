# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            leftMin, rightMin = float("inf"), float("inf")
            lMin, lMax, rMin, rMax = float("inf"), -float("inf"), float("inf"), -float("inf")
            if root.left is not None:
                lMin, lMax, lMinDiff = dfs(root.left)
                leftMin = min(abs(root.val - root.left.val), abs(root.val - lMin), abs(root.val - lMax), lMinDiff)
            if root.right is not None:
                rMin, rMax, rMinDiff = dfs(root.right)
                rightMin = min(abs(root.val - root.right.val), abs(root.val - rMin), abs(root.val - rMax), rMinDiff)
            return min(lMin, rMin, root.val), max(lMax, rMax, root.val), min(leftMin, rightMin)
        return dfs(root)[2]
        
