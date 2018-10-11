class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans, n = [], len(nums) + 1
        if n == 2:
            return ans
        for num in nums:
            num = num % n
            count, here = nums[num - 1] // n, nums[num - 1] % n
            if count == 1:
                ans.append(num)
            nums[num - 1] = (count + 1) * n + here
        #print(nums)
        return ans
    
