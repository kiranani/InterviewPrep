class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        v, a = set(), []
        def dfs(s):
            for x in map(str, range(k)):
                nei = s + x
                if nei not in v:
                    v.add(nei)
                    dfs(nei[1:])
                    a.append(x)
        nei = "0" * (n - 1)
        dfs(nei)
        return "".join(a) + nei
        
