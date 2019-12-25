class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = [(float("inf"), -float("inf"))]
        

    def push(self, x: int) -> None:
        self.l.append((x, max(x, self.l[-1][1])))
        

    def pop(self) -> int:
        return self.l.pop()[0]
        

    def top(self) -> int:
        return self.l[-1][0]
        

    def peekMax(self) -> int:
        return self.l[-1][1]
        

    def popMax(self) -> int:
        mx, s = self.peekMax(), []
        while self.l[-1][0] != mx:
            s.append(self.l.pop()[0])
        self.l.pop()
        while s:
            self.push(s.pop())
        return mx


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
