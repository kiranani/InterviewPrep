from collections import defaultdict
from random import randint
class Solution:

    def __init__(self, nums: List[int]):
        self.h = defaultdict(list)
        for i, num in enumerate(nums):
            self.h[num].append(i)
        

    def pick(self, target: int) -> int:
        return self.h[target][randint(0, len(self.h[target]) - 1)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
