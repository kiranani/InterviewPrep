class RLEIterator:

    def __init__(self, A: List[int]):
        self.a = A
        self.n = len(A)
        for i in range(2, self.n, 2):
            self.a[i] += self.a[i - 2]
        self.l = 0
        self.i = 0
    
    
    def bs(self):
        r = self.n - 2
        while self.l < r:
            m = 2 * ((self.l + r) // 4)
            if self.i <= self.a[m]:
                r = m
            else:
                self.l = m + 2
        self.l = r

        
    def next(self, n: int) -> int:
        self.i += n
        self.bs()
        if self.i <= self.a[self.l]:
            return self.a[self.l + 1]
        return -1


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
