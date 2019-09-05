class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        t = [nums[0], float("inf")]
        for num in nums[1:]:
            if num < t[0]:
                t[0] = num
            elif t[1] > num > t[0]:
                t[1] = num
            elif num > t[1] > t[0]:
                return True
        return False
