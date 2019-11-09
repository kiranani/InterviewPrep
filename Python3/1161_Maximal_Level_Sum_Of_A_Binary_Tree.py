# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        mx, q = [], [(root, 0)]
        while q:
            n, l = q.pop()
            if len(mx) == l:
                mx.append(n.val)
            else:
                mx[l] += n.val
            if n.left:
                q.append((n.left, l + 1))
            if n.right:
                q.append((n.right, l + 1))
        i, m = 0, mx[0]
        for j, s in enumerate(mx[1:]):
            if s > m:
                i, m = j + 1, s
        return i + 1
        
            
        
