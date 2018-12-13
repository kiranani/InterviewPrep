class Solution:
    def twoSum(self, nums, target):
        numDict = {}
        for i, x in enumerate(nums):
            diff = numDict.get(target - x)
            if diff is not None:
                return [diff, i]
            numDict[x] = i
        
