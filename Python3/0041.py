class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i, np1 = 0, len(nums) + 1
        for num in nums:
            if 0 < num < np1:
                nums[i] = num
                i += 1
        for num in nums[:i]:
            if num <= i and nums[num - 1] > 0:
                nums[num - 1] = -nums[num - 1]
        for j, num in enumerate(nums[:i]):
            if num > 0:
                return j + 1
        return i + 1
