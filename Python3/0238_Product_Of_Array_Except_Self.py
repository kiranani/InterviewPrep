class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r, ans = 1, 1, [1] * n
        for i in range(n):
            ans[i] *= l
            l *= nums[i]
            ans[~i] *= r
            r *= nums[~i]
        return ans
        
