class Solution:
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        i, n, ans = 0, len(nums), []
        while i < n:
            #print(lower)
            start = i
            while i < n - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1
            if lower + 1 == nums[start]:
                ans.append(str(lower))
            elif lower < nums[start] - 1:
                ans.append(str(lower) + "->" + str(nums[start] - 1))
            lower = nums[i] + 1
            i += 1
        if lower == upper:
            ans.append(str(lower))
        elif lower < upper:
            ans.append(str(lower) + "->" + str(upper))
        return ans
