class StringIterator:

    def __init__(self, compressedString: str):
        self.s, self.i, self.n = compressedString, 0, len(compressedString)
        self.ch, self.c = self.compute()
        
        
    def compute(self):
        ch, c = " ", 0
        if self.i < self.n:
            ch = self.s[self.i]
            self.i += 1
            while self.i < self.n and self.s[self.i].isdigit():
                c = 10 * c + int(self.s[self.i])
                self.i += 1
        return ch, c
        
        
    def next(self) -> str:
        ch = self.ch
        if self.hasNext():
            self.c -= 1
            if not self.c:
                self.ch, self.c = self.compute()
        return ch

    def hasNext(self) -> bool:
        return self.ch != " "


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
