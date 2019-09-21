class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        p, s = 1, min(N - K + 1, W)
        q = collections.deque([1] * s)
        for i in range(K - 1, -1, -1):
            p = s / W
            s += p
            q.appendleft(p)
            if len(q) > W:
                s -= q.pop()
        return p
                
        
