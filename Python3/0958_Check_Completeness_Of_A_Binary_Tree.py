# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        i, nodes = 0, [(root, 1)]
        while i < len(nodes):
            i, node = i + 1, nodes[i]
            if node[0]:
                nodes.append((node[0].left, 2 * node[1]))
                nodes.append((node[0].right, 2 * node[1] + 1))
            if nodes[-1][1] != len(nodes):
                return False
        return True
        
