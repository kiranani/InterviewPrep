class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        g = collections.defaultdict(list)
        for edge in times:
            g[edge[0]].append((edge[2], edge[1]))
                
        def dfs(s, t):
            if t >= n[s - 1]:
                return
            n[s - 1] = t
            g[s].sort()
            for e, d in g[s]:
                dfs(d, t + e)
                
        INF = float("inf")
        n = [INF] * N
        dfs(K, 0)
        m = max(n)
        return -1 if m == INF else m
                
                
