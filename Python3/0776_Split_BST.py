# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def splitBST(self, root: TreeNode, V: int) -> List[TreeNode]:
        if not root:
            return [None, None]
        elif root.val <= V:
            splits = self.splitBST(root.right, V)
            root.right = splits[0]
            return [root, splits[1]]
        else:
            splits = self.splitBST(root.left, V)
            root.left = splits[1]
            return [splits[0], root]
        
        
