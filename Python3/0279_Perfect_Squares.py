class Solution:
    def numSquares(self, n: int) -> int:
        def isPossible(k, c):
            if c == 1:
                return k in sq
            for s in sq:
                if s < k and isPossible(k - s, c - 1):
                    return True
            return False
                    
        sq = [i * i for i in range(1, 1 + int(n ** 0.5))]
        
        # Every positive integer can be written as sum of 4 squares
        for i in range(1, 4):
            if isPossible(n, i):
                return i
        return 4
        
        
        
        
