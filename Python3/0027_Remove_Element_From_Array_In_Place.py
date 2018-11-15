class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        def bubble(ind):
            while ind < n - c - 1:
                nums[ind], nums[ind + 1] = nums[ind + 1], nums[ind]
                ind += 1
        n = len(nums)
        if n == 0:
            return 0
        i, j, c = 0, n - 1, 0
        while j > -1:
            while j > -1 and nums[j] != val:
                j -= 1
            if j > -1:
                bubble(j)
                c += 1
                j -= 1
        return n - c
        
