"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        clones, q = {node: Node(node.val, [])}, collections.deque([node])
        while q:
            n = q.popleft()
            for nei in n.neighbors:
                if nei not in clones:
                    clones[nei] = Node(nei.val, [])
                    q.append(nei)
                clones[n].neighbors.append(clones[nei])
        return clones[node]
                
        
