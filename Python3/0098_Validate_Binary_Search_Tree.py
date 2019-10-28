# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode, low = -float("inf"), high = float("inf")) -> bool:
        if not root:
            return True
        else:
            if root.val >= high or root.val <= low:
                return False
            return (self.isValidBST(root.left, low, root.val) 
                    and self.isValidBST(root.right, root.val, high))
        
