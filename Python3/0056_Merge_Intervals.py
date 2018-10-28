# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        points = []
        for point in intervals:
            points.append([point.start, 0])
            points.append([point.end, 1])
        points.sort(key=operator.itemgetter(0))
        s, ints, prev = [], [], points[0][0]
        for point in points:
            if point[1] == 0:
                s.append(point[0])
            else:
                if len(s) == 1:
                    start = s.pop()
                    if len(ints) and start == ints[-1].end:
                        ints[-1].end = point[0]
                    else:
                        ints.append(Interval(start, point[0]))
                else:
                    s.pop()
        return ints

    
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        def intersect(a, b):
            return a.end >= b.start
        intervals.sort(key=lambda x: (x.start, -x.end))
        #print([(x.start, x.end) for x in intervals])
        ints = [intervals[0]]
        for interval in intervals[1:]:
            #print(interval.start, interval.end, ints[-1].start, ints[-1].end)
            if intersect(ints[-1], interval):
                ints[-1].end = max(ints[-1].end, interval.end)
            else:
                ints.append(interval)
        return ints
                    
