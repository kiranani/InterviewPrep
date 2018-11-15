class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        n, h = len(wall), collections.Counter()
        for row in wall:
            s = 0
            for brick in row[:-1]:
                s += brick
                h[s] = h[s] + 1
        if h:
            return n - h.most_common(1)[0][1]
        else:
            return n
        
