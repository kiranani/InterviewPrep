# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def helper(root):
            if not root:
                return 0
            nonlocal maxSum
            leftSum, rightSum = max(0, helper(root.left)), max(0, helper(root.right))
            maxSum = max(maxSum, leftSum + root.val + rightSum)
            return root.val + max(rightSum, leftSum)
        maxSum = -float("inf")
        helper(root)
        return maxSum
        
