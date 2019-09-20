class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        ch = [i for i in range(n) if seats[i]]
        m = max(ch[0], n - ch[-1] - 1)
        for i in range(1, len(ch)):
            m = max(m, (ch[i] - ch[i - 1]) // 2)
        return m
            
        
