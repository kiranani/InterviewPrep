# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        def bfs(arr):
            if arr:
                children, nums = [], []
                for n in arr:
                    if n.left:
                        children.append(n.left)
                    if n.right:
                        children.append(n.right)
                    nums.append(n.val)
                ans.append(nums)
                bfs(children)
        bfs([root])
        return ans
        
