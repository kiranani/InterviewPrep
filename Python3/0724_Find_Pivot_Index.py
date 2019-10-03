class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l, s = 0, sum(nums)
        for i, num in enumerate(nums):
            if l == s - l - num:
                return i
            l += num
        return -1
        
