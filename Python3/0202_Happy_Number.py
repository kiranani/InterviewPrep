class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n not in s:
            if n == 1:
                return True
            s.add(n)
            sq = 0
            while n:
                n, r = divmod(n, 10)
                sq += r * r
            n = sq
        return False
        
