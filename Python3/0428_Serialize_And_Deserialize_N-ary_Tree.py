"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return ""
        elif not root.children:
            return str(root.val)
        else:
            ch = [self.serialize(x) for x in root.children]
            return "{}({})".format(root.val, ",".join(ch))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        i, n = 0, len(data)
        def helper(i):
            siblings, val, children = [], 0, []
            while i < n:
                c = data[i]
                if c.isdigit():
                    val = 10 * val + int(c)
                elif c == "(":
                    i, children = helper(i + 1)
                else:
                    siblings.append(Node(val, children))
                    if c == ")": break
                    val, children = 0, []
                i += 1
            if i == n:
                siblings.append(Node(val, children))
            return i, siblings
        return helper(0)[1][0]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
