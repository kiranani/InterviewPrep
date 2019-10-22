from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c, d, s = 0, defaultdict(int), 0
        d[0] = 1
        for num in nums:
            s += num
            if d.get(s - k):
                c += d[s - k]
            d[s] += 1
        return c
