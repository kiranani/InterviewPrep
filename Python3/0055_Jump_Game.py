class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        j, p = n - 2, n - 1
        while j > -1:
            if p - j <= nums[j]:
                p = j
            j -= 1
        return p == 0
        
