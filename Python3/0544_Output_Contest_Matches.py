class Solution:
    def findContestMatch(self, n: int) -> str:
        match_format = "({},{})"
        q = [match_format.format(i + 1, n - i) for i in range(n >> 1)]
        n >>= 1
        while n > 1:
            q = [match_format.format(q[i], q[n - i - 1]) for i in range(n >> 1)]
            n >>= 1
        return q[0]
        
        
