# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    count = 0
    def recurse(self, root, sum):
        if root == None:
            return []
        if root.val == sum:
            self.count += 1
        cases = self.recurse(root.left, sum) + self.recurse(root.right, sum)
        for i, case in enumerate(cases):
            if case + root.val == sum:
                self.count += 1
            cases[i] += root.val
        return cases + [root.val]

    def pathSum(self, root, sum):
        print(self.recurse(root, sum))
        return self.count
  
