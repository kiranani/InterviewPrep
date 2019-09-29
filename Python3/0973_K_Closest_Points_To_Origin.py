class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        n = len(points)
        if n <= K:
            return points
        heap = []
        for i in range(K):
            d = points[i][0] ** 2 + points[i][1] ** 2
            heapq.heappush(heap, [-d, points[i]])
        for i in range(K, n):
            d = points[i][0] ** 2 + points[i][1] ** 2
            heapq.heappushpop(heap, [-d, points[i]])
        return [x[1] for x in heap]
        
