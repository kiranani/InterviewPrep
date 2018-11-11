class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #x = 0
        #for num in nums:
        #    x ^= num
        #return x
        i, n = 0, len(nums)
        while i < n:
            if i + 1 < n and nums[i] == nums[i + 1]:
                i += 2
            else:
                return nums[i]
                
