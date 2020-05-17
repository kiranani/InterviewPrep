# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        if root:
            s = [root]
            while s:
                node = s.pop()
                if node.right:
                    s.append(node.right)
                if node.left:
                    s.append(node.left)
                ans.append(node.val)
        return ans
        
        
