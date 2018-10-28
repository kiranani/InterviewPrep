# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        def intersect(a, b):
            return a.end > b.start
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda x: (x.start, x.end))
        print([(x.start, x.end) for x in intervals])
        c, meeting = 0, intervals[0]
        for interval in intervals[1:]:
            if intersect(meeting, interval):
                c += 1
                meeting = meeting if meeting.end <= interval.end else interval
            else:
                meeting = interval
        return c
        
        
