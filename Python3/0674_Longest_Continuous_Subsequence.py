class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j, length, n = 0, 1, 1, len(nums)
        if n == 0:
            return 0
        while j < n:
            curLength = 1
            while j < n and nums[i] < nums[j]:
                i += 1
                j += 1
                curLength += 1
            length = length if length > curLength else curLength
            i, j = j, j + 1
        return length
    
