class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        r, h, m = 0, {0: -1}, 0
        for i, c in enumerate(nums):
            r += c if c else -1
            if r in h:
                m = max(m, i - h[r])
            else:
                h[r] = i
        return m
        
