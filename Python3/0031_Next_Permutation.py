class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, n = 0, len(nums)
        while i < n - 1 and nums[~i] <= nums[~(i + 1)]:
            i += 1
        if i < n - 1:
            j = i + 1
            while i > -1 and nums[~i] > nums[~j]:
                i -= 1
            i += 1
            nums[~j], nums[~i] = nums[~i], nums[~j]
            i = j - 1
        j = 0
        while i > j:
            nums[~i], nums[~j] = nums[~j], nums[~i]
            i, j = i - 1, j + 1
        
