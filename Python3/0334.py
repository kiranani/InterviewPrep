class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        mins, l = [float("inf")] * 2, 0
        for num in nums:
            #print(mins)
            if l == 0:
                mins[0], l = num, 1
            elif l == 1:
                if num > mins[0]:
                    mins[1], l = num, 2
                elif num < mins[0]:
                    mins[0] = num
            elif l == 2:
                if num > mins[1]:
                    return True
                elif num > mins[0]:
                    mins[1] = num
                elif num < mins[0]:
                    mins[0] = num
        return False
    
