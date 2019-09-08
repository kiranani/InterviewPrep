class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        class BST:
            def __init__(self, v):
                self.val = v
                self.count = 1
                self.leftCount = 0
                self.left = self.right = None
           
            def insert(self, v, c):
                if v == self.val:
                    self.count += 1
                    c += self.leftCount
                elif v > self.val:
                    c += self.count + self.leftCount
                    if self.right:
                        return self.right.insert(v, c)
                    else:
                        self.right = BST(v)
                else:
                    self.leftCount += 1
                    if self.left:
                        return self.left.insert(v, c)
                    else:
                        self.left = BST(v)
                return c
            
        n = len(nums)
        if not n:
            return []
        r, ans = BST(nums[-1]), [0] * n
        for i in range(1, n):
            ans[~i] = r.insert(nums[~i], 0)
        return ans
                
