"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        def bfs(q):
            c = collections.deque()
            while len(q) > 1:
                n = q.popleft()
                n.next = q[0]
                if n.left:
                    c.append(n.left)
                if n.right:
                    c.append(n.right)
            if not c:
                return
            c.append(None)
            bfs(c)
        q = collections.deque([root, None])
        bfs(q)
        return root
        
