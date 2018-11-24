class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def minInd(arr, target):
            i, j = 0, len(arr) - 1
            while i < j:
                m = (i + j) // 2
                if target == arr[m]:
                    j = m
                elif target < arr[m]:
                    j = m - 1
                else:
                    i = m + 1
            return i

        def maxInd(arr, target):
            i, j = 0, len(arr) - 1
            while i < j:
                m = (i + j + 1) // 2
                if target == arr[m]:
                    i = m
                elif target < arr[m]:
                    j = m - 1
                else:
                    i = m + 1
            return i
        
        mi = minInd(nums, target)
        if mi < len(nums) and mi > -1 and nums[mi] == target:
            ma = maxInd(nums, target)
            return [mi, ma]
        else:
            return [-1, -1]
