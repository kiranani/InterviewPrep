class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.h = []
        

    def truncateLogs(self, time):
        while self.h and self.h[0][0] < time:
            m = heapq.heappop(self.h)[1]
            if self.d[m] < time:
                del self.d[m]
        
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        printMessage = timestamp > self.d.get(message, -1)
        if printMessage:
            self.d[message] = timestamp + 9
            heapq.heappush(self.h, (timestamp + 9, message))
        self.truncateLogs(timestamp)
        return printMessage


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
