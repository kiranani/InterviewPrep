class Solution:
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def intersect(a, b):
            return a[1] >= b[0]
        if len(points) == 0:
            return 0
        points.sort(key=lambda x: (x[0], -x[1]))
        #print(points)
        a, b = 0, points[0]
        for point in points[1:]:
            if intersect(b, point):
                b = [max(b[0], point[0]), min(b[1], point[1])]
            else:
                b = point
                a += 1
        return a + 1
