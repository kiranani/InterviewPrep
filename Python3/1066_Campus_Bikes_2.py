class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        n, m, v = len(workers), len(bikes), {}
        def backtrack(i, k):
            if i == n:
                return 0
            elif k in v:
                return v[k]
            mn = float("inf")
            for j in range(m):
                if ((1 << j) & k) == 0:
                    k |= 1 << j
                    dj = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                    mn = min(mn, dj + backtrack(i + 1, k))
                    k &= ~(1 << j)
            v[k] = mn
            return mn
        return backtrack(0, 0)

                                        
        
