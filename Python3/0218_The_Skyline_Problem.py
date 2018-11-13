class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return []
        points = [(x[0], -x[2], x[1]) for x in buildings] + [(x[1], 0, 0) for x in buildings]
        points.sort()
        ans, heap = [[0, 0]], [(0, float("inf"))]
        for point in points:
            while point[0] >= heap[0][1]:
                heapq.heappop(heap)
            if point[1]:
                heapq.heappush(heap, (point[1], point[2]))
            if ans[-1][1] != -heap[0][0]:
                ans.append([point[0], -heap[0][0]])
        return ans[1:]
