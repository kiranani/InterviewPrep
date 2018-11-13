# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.start)
        for i, interval in enumerate(intervals[:-1]):
            if interval.end > intervals[i + 1].start:
                return False
        return True
        
