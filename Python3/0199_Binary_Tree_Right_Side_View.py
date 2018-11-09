# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        else:
            rView = self.rightSideView(root.right)
            lView = self.rightSideView(root.left)
            if len(rView) < len(lView):
                return [root.val] + rView + lView[len(rView):]
            else:
                return [root.val] + rView
            
