# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if p.right:
            node = p.right
            while node.left:
                node = node.left
            return node
        else:
            node, q, s = root, [], []
            while node:
                while node:
                    s.append(node)
                    node = node.left
                while not node and s:
                    node = s.pop()
                    if q and q[-1] == p:
                        return node
                    q.append(node)
                    node = node.right
            return None
            
