# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        left, right = [], []
        q = collections.deque([(0, root)])
        while q:
            index, node = q.popleft()
            l = left if index < 0 else right
            l_index = abs(index) - 1 if index < 0 else index
            if len(l) <= l_index:
                l.append([])
            l[l_index].append(node.val)
            if node.left:
                q.append((index - 1, node.left))
            if node.right:
                q.append((index + 1, node.right))
        return left[::-1] + right
            
                
        
        
