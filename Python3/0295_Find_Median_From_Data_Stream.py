class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mn = self.mx = 0
        self.minH = [] # To store larger numbers
        self.maxH = [] # To store smaller numbers
        

    def addNum(self, num: int) -> None:
        if self.mn + self.mx == 0:
            heapq.heappush(self.minH, num)
            self.mn += 1
        elif self.mn > self.mx:
            self.mx += 1
            if num > self.minH[0]:
                heapq.heappush(self.maxH, -heapq.heappop(self.minH))
                heapq.heappush(self.minH, num)
            else:
                heapq.heappush(self.maxH, -num)
        elif self.mx > self.mn:
            self.mn += 1
            if num < -self.maxH[0]:
                heapq.heappush(self.minH, -heapq.heappop(self.maxH))
                heapq.heappush(self.maxH, -num)
            else:
                heapq.heappush(self.minH, num)
        else:
            if num > self.minH[0]:
                heapq.heappush(self.minH, num)
                self.mn += 1
            else:
                heapq.heappush(self.maxH, -num)
                self.mx += 1
        

    def findMedian(self) -> float:
        if self.mn > self.mx:
            return self.minH[0]
        elif self.mx > self.mn:
            return -self.maxH[0]
        else:
            return (self.minH[0] - self.maxH[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
