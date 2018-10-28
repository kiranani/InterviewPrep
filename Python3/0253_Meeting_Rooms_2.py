# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda x: x.start)
        rooms = [intervals[0].end]
        for interval in intervals[1:]:
            if interval.start >= rooms[0]:
                heapq.heappushpop(rooms, interval.end)
            else:
                heapq.heappush(rooms, interval.end)
        return len(rooms)
        
