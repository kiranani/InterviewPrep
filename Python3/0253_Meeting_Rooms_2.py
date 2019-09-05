class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: (x[0], x[1]))
        h = [intervals[0][1]]
        for interval in intervals[1:]:
            if h[0] <= interval[0]:
                heapq.heappop(h)
            heapq.heappush(h, interval[1])
        return len(h)
            
