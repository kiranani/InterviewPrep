# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(l, r):
            if l <= r:
                m = (l + r) // 2
                n = TreeNode(nums[m])
                n.right = helper(m + 1, r)
                n.left = helper(l, m - 1)
                return n
        return helper(0, len(nums) - 1)
        
