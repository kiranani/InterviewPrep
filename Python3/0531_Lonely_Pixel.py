class Solution:
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        m = len(picture)
        if m == 0:
            return 0
        n = len(picture[0])
        rows, cols = [0] * m, [0] * n
        for i in range(m):
            for j in range(n):
                if picture[i][j] == "B":
                    rows[i] += 1
                    cols[j] += 1
        return min(len([x for x in rows if x == 1]), len([x for x in cols if x == 1]))
        
