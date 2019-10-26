# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        stk, ans = [root], []
        while stk:
            node = stk.pop()
            if node:
                ans.append(str(node.val))
                stk.append(node.right)
                stk.append(node.left)
            else:
                ans.append("#")
        return " ".join(ans)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split()
        i, n = -1, len(vals)
        def recurse():
            nonlocal i
            i += 1
            if i == n:
                return
            elif vals[i] == "#":
                return
            else:
                node = TreeNode(int(vals[i]))
                node.left = recurse()
                node.right = recurse()
                return node
        return recurse()
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
