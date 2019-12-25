class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        if not picture:
            return 0
        m, n = len(picture), len(picture[0])
        rr, rc = [0] * m, [0] * n
        for i in range(m):
            for j in range(n):
                if picture[i][j] == "B":
                    rr[i] += 1
                    rc[j] += 1
        return min(rr.count(1), rc.count(1))
        
