class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        nSum = n * (n + 1) // 2
        for num in nums:
            num = abs(num)
            if nums[num - 1] < 0:
                repeated = num
            else:
                nSum -= num
                nums[num - 1] = -nums[num - 1]
            #print(nSum)
        return [repeated, nSum]
        
