class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [-float("inf")] + nums + [-float("inf")]
        n = len(nums)
        if n == 3:
            return 0
        i, j = 1, n - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m - 1] < nums[m] < nums[m + 1]:
                i = m + 1
            elif nums[m - 1] > nums[m] > nums[m + 1]:
                j = m - 1
            elif nums[m - 1] < nums[m] > nums[m + 1]:
                return m - 1
            else:
                i = m + 1
        return i
        
