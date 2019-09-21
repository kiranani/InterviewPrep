class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.n = size
        self.s = 0
        self.q = collections.deque()
        

    def next(self, val: int) -> float:
        self.s += val
        self.q.append(val)
        if len(self.q) > self.n:
            self.s -= self.q.popleft()
            return self.s / self.n
        else:
            return self.s / len(self.q)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
