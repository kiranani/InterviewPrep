"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        node, s, a = root, [], []
        while node or s:
            while node:
                s.append(node)
                node = node.left
            a.append(s.pop())
            if len(a) > 1:
                a[-2].right, a[-1].left = a[-1], a[-2]
            node = a[-1].right
        a[0].left, a[-1].right = a[-1], a[0]
        return a[0]
        
        
