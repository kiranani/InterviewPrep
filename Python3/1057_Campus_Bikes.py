class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        n = len(workers)
        if not workers:
            return []
        d, h = [], [[] for _ in range(n)]
        for i, w in enumerate(workers):
            for j, b in enumerate(bikes):
                heapq.heappush(h[i], (abs(b[0] - w[0]) + abs(b[1] - w[1]), i, j))
            heapq.heappush(d, heapq.heappop(h[i]))
        ans, bs = [None] * n, set()
        while len(bs) < n:
            x, w, b = heapq.heappop(d)
            if b in bs:
                heapq.heappush(d, heapq.heappop(h[w]))
            else:
                bs.add(b)
                ans[w] = b
        return ans
        
