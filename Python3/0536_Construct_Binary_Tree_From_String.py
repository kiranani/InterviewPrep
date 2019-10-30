# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def str2tree(self, s: str) -> TreeNode:
        n = len(s)
        def helper(i):
            root = None
            while i < n:
                c = s[i]
                if c.isdigit() or c == "-":
                    j = i + 1
                    while j < n and s[j].isdigit():
                        j += 1
                    root = TreeNode(int(s[i:j]))
                    i = j - 1
                elif c == "(":
                    i, child = helper(i + 1)
                    if not root.left:
                        root.left = child
                    else:
                        root.right = child
                else:
                    return i, root
                i += 1
            return i, root
        return helper(0)[1]
        
