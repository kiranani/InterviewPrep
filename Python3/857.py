class Solution:
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        n, w = len(wage), float('inf')
        ratios = sorted([[wage[i] / quality[i], quality[i]] for i in range(n)])
        l, qt = [], 0
        for r, q in ratios:
            heapq.heappush(l, -q)
            qt += q
            if len(l) > K:
                qt += heapq.heappop(l)
            if len(l) == K:
                w = min(w, qt * r)
        return w
        
