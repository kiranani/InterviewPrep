from heapq import heapify, heappush, heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapify(stones)
        while len(stones) > 1:
            stone1, stone2 = heappop(stones), heappop(stones)
            if stone1 != stone2:
                heappush(stones, stone1 - stone2)
        return -stones[0] if stones else 0
