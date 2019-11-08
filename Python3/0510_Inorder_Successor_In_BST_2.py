"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
"""
class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if node:
            if node.right:
                node = node.right
                while node.left:
                    node = node.left
                return node
            else:
                par = node.parent
                while par and node == par.right:
                    node = par
                    par = node.parent
                return par
        return None
        
