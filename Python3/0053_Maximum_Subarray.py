class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s, m = nums[0], nums[0]
        for num in nums[1:]:
            s = s + num if num + s > num else num
            m = s if s > m else m
        return m
