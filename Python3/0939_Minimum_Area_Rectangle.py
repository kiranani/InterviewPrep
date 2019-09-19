class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        if len(points) < 4:
            return 0
        g = collections.defaultdict(set)
        for point in points:
            g[point[0]].add(point[1])
        m, l = float("inf"), list(g.keys())
        for i in range(len(l)):
            for j in range(i + 1, len(l)):
                x1, x2 = l[i], l[j]
                ys = sorted(g[x1].intersection(g[x2]))
                if len(ys) > 1:
                    dy = [ys[i + 1] - ys[i] for i in range(len(ys) - 1)]
                    m = min(m, abs(x1 - x2) * min(dy))
        if m < float("inf"):
            return m
        return 0
        
