class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m, s = 0, set(nums)
        for n in s:
            if n - 1 not in s:
                c, l = n, 1
                while c + 1 in s:
                    c += 1
                    l += 1
                m = max(m, l)
        return m
        
