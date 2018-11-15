class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, n = 1, len(nums)
        if n == 0:
            return 0
        for j in range(1, n):
            if nums[i - 1] != nums[j]:
                nums[i] = nums[j]
                i += 1
        return i
        
