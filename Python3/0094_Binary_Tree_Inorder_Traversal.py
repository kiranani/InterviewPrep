# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        if root:
            s, node = [], root
            while node:
                while node:
                    s.append(node)
                    node = node.left
                while not node and s:
                    node = s.pop()
                    ans.append(node.val)
                    node = node.right
        return ans
        
