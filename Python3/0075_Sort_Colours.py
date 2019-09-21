class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l, r = 0, n - 1
        while l < n and nums[l] == 0:
            l += 1
        while r > -1 and nums[r] == 2:
            r -= 1
        i = l
        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], 0
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], 2
                r -= 1
            else:
                i += 1
        
