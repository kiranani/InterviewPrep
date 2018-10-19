class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n == 0 or k < 1:
            return 0
        p, i, j, c = 1, 0, 0, 0
        while j < n:
            #print(i, j, p)
            p *= nums[j]
            while p >= k and i <= j:
                p //= nums[i]
                i += 1
            c += j - i + 1
            j += 1
        return c
        
