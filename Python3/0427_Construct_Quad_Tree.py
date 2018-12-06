"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        n = len(grid)
        def make(x, y, s):
            if s == 1:
                return Node(grid[x][y] == 1, True, None, None, None, None)
            else:
                ns = s // 2
                tl, tr = make(x, y, ns), make(x, y + ns, ns)
                bl, br = make(x + ns, y, ns), make(x + ns, y + ns, ns)
                if tl.val == tr.val == bl.val == br.val and tl.val != "*":
                    return Node(tl.val, True, None, None, None, None)
                else:
                    return Node("*", False, tl, tr, bl, br)
        return make(0, 0, n)
        
