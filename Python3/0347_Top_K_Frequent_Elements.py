class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d, h = collections.Counter(nums), []
        for key in d:
            heapq.heappush(h, (d[key], key))
            if len(h) > k:
                heapq.heappop(h)
        return [x[1] for x in h]
        
