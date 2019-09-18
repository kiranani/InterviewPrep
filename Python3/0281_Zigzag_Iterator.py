class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.lists = [v1, v2]
        self.lc = len(self.lists)
        self.counts = [len(x) for x in self.lists]
        m, mi = 0, 0
        for i, c in enumerate(self.counts):
            if c >= m:
                m, mi = c, i
        self.m = self.lc * (m - 1) + mi + 1
        self.i = 0
        

    def next(self):
        """
        :rtype: int
        """
        n = self.get()
        while self.i < self.m and n is None:
            self.i += 1
            n = self.get()
        self.i += 1
        return n
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i < self.m
    
    
    def get(self):
        i, v = divmod(self.i, self.lc)
        if i < self.counts[v]:
            return self.lists[v][i]
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
