# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        a, q, l = [], collections.deque([root]), 0
        if root:
            ll = 1
            while ll:
                a.append([])
                c = 0
                while c < ll:
                    n = q.popleft()
                    a[l].append(n.val)
                    if n.left: q.append(n.left)
                    if n.right: q.append(n.right)
                    c += 1
                ll = len(q)
                l += 1
        return a
        
