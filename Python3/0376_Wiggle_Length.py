class Solution:
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        u, d, n = 1, 1, len(nums)
        if n == 0:
            return 0
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                u = d + 1
            elif nums[i - 1] > nums[i]:
                d = u + 1
            #print(u, d)
        return max(u, d)
