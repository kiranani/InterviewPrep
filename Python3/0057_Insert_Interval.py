# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]
        elif intervals[0].start > newInterval.end:
            return [newInterval] + intervals
        elif newInterval.start > intervals[-1].end:
            return intervals + [newInterval]
        ans, n, i, merged = [], len(intervals), 0, False
        while i < n:
            if not merged and intervals[i].end < newInterval.start:
                ans.append(intervals[i])
            elif not merged and newInterval.end < intervals[i].start:
                ans.extend([newInterval, intervals[i]])
                merged = True
            elif merged:
                ans.append(intervals[i])
            else:
                start = min(newInterval.start, intervals[i].start)
                while i < n and newInterval.end >= intervals[i].start:
                    i += 1
                i -= 1
                end = max(newInterval.end, intervals[i].end)
                ans.append(Interval(start, end))
                merged = True
            i += 1
        return ans
