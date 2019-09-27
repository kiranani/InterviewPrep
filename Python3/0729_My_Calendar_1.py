class Tree:
    def __init__(self, s, e):
        self.start = s
        self.end = e
        self.left = self.right = None
    
    def insert(self, s, e):
        if self.end <= s:
            if self.right:
                return self.right.insert(s, e)
            else:
                self.right = Tree(s, e)
        elif self.start >= e:
            if self.left:
                return self.left.insert(s, e)
            else:
                self.left = Tree(s, e)
        else:
            return False
        return True

class MyCalendar:     
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if self.root:
            return self.root.insert(start, end)
        self.root = Tree(start, end)
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
