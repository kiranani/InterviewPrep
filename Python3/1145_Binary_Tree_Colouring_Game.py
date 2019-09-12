# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: TreeNode
        :type n: int
        :type x: int
        :rtype: bool
        """
        def find(root):
            if not root:
                return 0, None
            elif root.val == x:
                return 0, root
            else:
                lc, lr = find(root.left)
                rc, rr = find(root.right)
                return 1 + lc + rc, lr or rr
            
        def count(root):
            if not root:
                return 0
            return 1 + count(root.left) + count(root.right)
        
        w = n // 2
        c, n = find(root)
        if c > w:
            return True
        lc, rc = count(n.left), count(n.right)
        return lc > w or rc > w
        
