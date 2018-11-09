class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []
        p1, p2, ans = 1, 1, [1] * len(nums)
        for i in range(n - 1):
            p1 *= nums[i]
            p2 *= nums[-i - 1]
            ans[i + 1] *= p1
            ans[-i - 2] *= p2
        return ans
        
