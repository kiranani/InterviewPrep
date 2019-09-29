# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        n, nn = [], []
        q = collections.deque([(root, 0, 0)])
        while q:
            node, x, y = q.popleft()
            if x < 0:
                i = -1 - x
                if len(n) == i:
                    n.append([(y, node.val)])
                else:
                    n[i].append((y, node.val))
            else:
                if len(nn) == x:
                    nn.append([(y, node.val)])
                else:
                    nn[x].append((y, node.val))
            if node.left:
                q.append((node.left, x - 1, y + 1))
            if node.right:
                q.append((node.right, x + 1, y + 1))
        return [[y[1] for y in sorted(x)] for x in n[::-1] + nn]
        
