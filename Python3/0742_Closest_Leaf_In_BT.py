# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        closest = [float("inf"), None]
        def findClosest(node, d):
            if node is None or d >= closest[0]:
                return
            elif node.left is None and node.right is None and d < closest[0]:
                closest[0] = d
                closest[1] = node
            else:
                findClosest(node.left, d + 1)
                findClosest(node.right, d + 1)
        def findK(node, arr):
            if node is None:
                return
            elif node.val == k:
                return [(node, 0)] + arr
            else:
                return findK(node.left, [(node, 1)] + arr) or findK(node.right, [(node, 2)] + arr)
        arr = findK(root, [])
        if arr[0][0].left is None and arr[0][0].right is None:
            return arr[0][0].val
        findClosest(arr[0][0].left, 1)
        findClosest(arr[0][0].right, 1)
        for i, e in enumerate(arr[1:]):
            if e[1] == 1:
                findClosest(e[0].right, i + 2)
            else:
                findClosest(e[0].left, i + 2)
        return closest[1].val
        
        
