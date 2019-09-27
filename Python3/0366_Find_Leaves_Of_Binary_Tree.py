# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        def collectAndRemove(node, ans):
            m = 0
            if node.left:
                m = max(m, collectAndRemove(node.left, ans))
            if node.right:
                m = max(m, collectAndRemove(node.right, ans))
            if len(ans) < m + 1:
                ans.append([node.val])
            else:
                ans[m].append(node.val)
            return m + 1
        collectAndRemove(root, ans)
        return ans
        
