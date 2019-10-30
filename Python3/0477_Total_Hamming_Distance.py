class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        counts = [0] * 32
        for n in nums:
            i = 0
            while n:
                counts[i] += n & 1
                n >>= 1
                i += 1
        n = len(nums)
        return sum([x * (n - x) for x in counts])
    
