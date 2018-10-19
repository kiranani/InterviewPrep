class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        minLen, i, curSum = float("inf"), 0, 0
        for j, num in enumerate(nums):
            curSum += num
            while curSum >= s:
                curLen = j - i + 1
                minLen = minLen if minLen < curLen else curLen
                curSum -= nums[i]
                i += 1
        return minLen if minLen < n + 1 else 0
     
