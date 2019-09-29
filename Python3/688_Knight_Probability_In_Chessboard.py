class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        moves = [(1, 2), (-1, 2), (1, -2), (-1, -2), 
                 (2, 1), (-2, 1), (2, -1), (-2, -1)]
        memo, p8th = {}, 0.125
        def dfs(i, j, k):
            if -1 < i < N and -1 < j < N:
                if k == K:
                    return 1
                elif (i, j, k) in memo:
                    return memo[i, j, k]
                p = 0
                for di, dj in moves:
                    mi, mj = i + di, j + dj
                    p += p8th * dfs(mi, mj, k + 1)
                memo[i, j, k] = memo[j, i, k] = p
                memo[N - i - 1, j, k] = memo[j, N - i - 1, k] = p
                memo[i, N - j - 1, k] = memo[N - j - 1, i, k] = p
                memo[N - i - 1, N - j - 1, k] = memo[N - j - 1, N - i - 1, k] = p
                return p
            return 0
        return dfs(r, c, 0)
