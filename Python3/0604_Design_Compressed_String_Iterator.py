class StringIterator:

    def __init__(self, compressedString: str):
        self.counts = []
        i, n = 0, len(compressedString)
        while i < n:
            ch, c = compressedString[i], 0
            i += 1
            while i < n and compressedString[i].isdigit():
                c = 10 * c + int(compressedString[i])
                i += 1
            self.counts.append([ch, c])
        self.i = 0
        

    def next(self) -> str:
        ch = " "
        if self.hasNext():
            self.counts[self.i][1] -= 1
            ch = self.counts[self.i][0]
            if self.counts[self.i][1] == 0:
                self.i += 1
        return ch

    def hasNext(self) -> bool:
        return self.counts[-1][-1]


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
