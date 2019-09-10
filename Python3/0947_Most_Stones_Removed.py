from collections import defaultdict
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def dfs(xd, yd, i, v):
            if i in v:
                return
            v.add(i)
            for j in xd[stones[i][0]]:
                dfs(xd, yd, j, v)
            for j in yd[stones[i][1]]:
                dfs(xd, yd, j, v)
            
        n, xd, yd = len(stones), defaultdict(set), defaultdict(set)
        for i in range(n):
            xd[stones[i][0]].add(i)
            yd[stones[i][1]].add(i)
        c, v = 0, set()
        for i in range(n):
            if i not in v:
                c += 1
                dfs(xd, yd, i, v)
        return n - c
        
