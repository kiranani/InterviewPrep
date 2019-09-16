class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort(); heaters.sort()
        i, n, m = 0, len(heaters), -float("inf")
        for h in houses:
            d = float("inf")
            while i < n and heaters[i] < h:
                d = min(d, h - heaters[i])
                i += 1
            if i < n and heaters[i] - h < d:
                d = heaters[i] - h
            else:
                i -= 1
            m = max(m, d)
        return m
               
