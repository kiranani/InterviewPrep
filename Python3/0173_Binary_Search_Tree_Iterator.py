# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stk = []
        self.node = root
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.node:
            while self.node:
                self.stk.append(self.node)
                self.node = self.node.left
        if self.stk:
            nxt = self.stk.pop()
            self.node = nxt.right
            return nxt.val
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.node or self.stk
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
