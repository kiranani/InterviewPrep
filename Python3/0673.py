class Solution:
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        lengths, counts = [1] * n, [1] * n
        for j in range(n):
            for i in range(j):
                if nums[i] < nums[j]:
                    if lengths[i] >= lengths[j]:
                        lengths[j] = lengths[i] + 1
                        counts[j] = counts[i]
                    elif lengths[i] + 1 == lengths[j]:
                        counts[j] += counts[i]
                    #print(i, j, lengths, counts)
        maxLength, count = 0, 0
        for i in range(n):
            if lengths[i] > maxLength:
                maxLength = lengths[i]
                count = counts[i]
            elif maxLength == lengths[i]:
                count += counts[i]            
        return count
            
        
