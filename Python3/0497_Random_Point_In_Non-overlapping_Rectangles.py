class Solution:

    def __init__(self, rects: List[List[int]]):
        self.areas = [0] * (len(rects) + 1)
        for i, (x1, y1, x2, y2) in enumerate(rects):
            self.areas[i + 1] = (x2 - x1 + 1) * (y2 - y1 + 1) + self.areas[i]
        self.rects = rects
        self.n = len(rects)
        

    def bs(self, t):
        l, r = 0, self.n
        while l <= r:
            m = (l + r) // 2
            if t == self.areas[m]:
                return m
            elif t < self.areas[m]:
                r = m - 1
            else:
                l = m + 1
        return l
    
    
    def pick(self) -> List[int]:
        r = random.randint(1, self.areas[-1])
        i = self.bs(r)
        rect = self.rects[i - 1]
        dy, dx = divmod(r - self.areas[i - 1] - 1, rect[2] - rect[0] + 1)
        return [rect[0] + dx, rect[1] + dy]
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
