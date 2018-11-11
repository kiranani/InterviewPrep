class Solution:
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        I = float("inf")
        if len(points) < 4:
            return 0
        m = I
        d = collections.defaultdict(set)
        for point in points:
            d[point[0]].add(point[1])
        keys = sorted(list(d.keys()))
        #print(d)
        for j in range(1, len(keys)):
            for i in range(j):
                yPoints = sorted(list(d[keys[i]] & d[keys[j]]))
                diffs = [yPoints[i + 1] - yPoints[i] for i in range(len(yPoints) - 1)]
                if not diffs:
                    continue
                else:
                    minG = min(diffs)
                    a = (keys[j] - keys[i]) * minG
                    m = m if m < a else a
        return 0 if m == I else m
        
