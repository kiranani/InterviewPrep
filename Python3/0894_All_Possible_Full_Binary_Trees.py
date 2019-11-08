# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if not N or N % 2 == 0:
            return None
        elif N == 1:
            return [TreeNode(0)]
        ans = []
        for i in range(1, N, 2):
            lTrees = self.allPossibleFBT(i)
            rTrees = self.allPossibleFBT(N - i - 1)
            for lTree in lTrees:
                for rTree in rTrees:
                    root = TreeNode(0)
                    root.left = lTree
                    root.right = rTree
                    ans.append(root)
        return ans
        
