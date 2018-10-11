# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        l = []
        def recurse(root, depth):
            if root is not None:
                if depth < len(l):
                    l[depth] = l[depth] if l[depth] > root.val else root.val
                else:
                    l.append(root.val)
                recurse(root.left, depth + 1)
                recurse(root.right, depth + 1)
        recurse(root, 0)
        return l
        
