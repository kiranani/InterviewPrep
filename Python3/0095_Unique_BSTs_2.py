# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def dfs(i, j):
            if j < i:
                return [None]
            allTrees = []
            for k in range(i, j + 1):
                leftTrees, rightTrees = dfs(i, k - 1), dfs(k + 1, j)
                for lTree in leftTrees:
                    for rTree in rightTrees:
                        root = TreeNode(k)
                        root.left, root.right = lTree, rTree
                        allTrees.append(root)
            return allTrees
        return dfs(1, n) if n > 0 else []
        
