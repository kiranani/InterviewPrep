# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        def findAbove(root, target):
            if not root:
                return []
            elif root.val == target.val:
                return [(root, 'p')]
            leftNodes = findAbove(root.left, target)
            rightNodes = findAbove(root.right, target)
            if len(rightNodes) > 0:
                nodes = [(root, 'l')]
                return rightNodes + nodes
            elif len(leftNodes) > 0:
                nodes = [(root, 'r')]
                return leftNodes + nodes
            else:
                return []
        def findK(root, k):
            if not root or k < 0:
                return []
            elif k == 0:
                return [root.val]
            else:
                return findK(root.left, k - 1) + findK(root.right, k - 1)
        nodes = findAbove(root, target)
        n = len(nodes)
        vals = []
        for i, (node, d) in enumerate(nodes):
            if K - i == 0:
                vals.append(node.val)
            elif d == 'p':
                vals.extend(findK(node.left, K - i - 1))
                vals.extend(findK(node.right, K - i - 1))
            elif d == 'r':
                vals.extend(findK(node.right, K - i - 1))
            elif d == 'l':
                vals.extend(findK(node.left, K - i - 1))
        return vals
            
        
