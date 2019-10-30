class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nzi, n = 0, len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[nzi], nums[i] = nums[i], nums[nzi]
                nzi += 1
        
            
        
        
