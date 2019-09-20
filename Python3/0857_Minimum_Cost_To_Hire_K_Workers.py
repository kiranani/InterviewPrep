class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        ratios = sorted([(w / q, w, q) for w, q in zip(wage, quality)])
        a, h, m = 0, [], float("inf")
        for ratio, w, q in ratios:
            a += q
            heapq.heappush(h, -q)
            if len(h) > K:
                a += heapq.heappop(h)
            if len(h) == K:
                m = min(m, a * ratio)
        return m
        
