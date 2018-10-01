class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def recurse(nums, index):
            if index == len(nums):
                return [[]]
            subsets = recurse(nums, index + 1)
            ans = [] + subsets
            for s in subsets:
                ans.append([nums[index]] + s)
            return ans
        
        return recurse(nums, 0)
