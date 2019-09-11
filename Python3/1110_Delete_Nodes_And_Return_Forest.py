# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        s = set(to_delete)
        def helper(node, s):
            if not node: return None, []
            if not s: return node, []
            node.left, lf = helper(node.left, s)
            node.right, rf = helper(node.right, s)
            if node.val in s:
                s.remove(node.val)
                if node.left:
                    lf.append(node.left)
                if node.right:
                    rf.append(node.right)
                node = None
            return node, lf + rf
        node, f = helper(root, s)
        if node:
            f.append(node)
        return f
        
