class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        while i > -1 and nums[i + 1] <= nums[i]:
            i -= 1
        if i > -1:
            j = i + 1
            while j < n and nums[i] < nums[j]:
                j += 1
            nums[i], nums[j - 1] = nums[j - 1], nums[i]
        i += 1
        for j in range((n - i) // 2):
            nums[i + j], nums[n - j - 1] = nums[n - j - 1], nums[i + j]
            
