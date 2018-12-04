class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.h = {}
        

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        x = self.h.get(message)
        if x is None:
            self.h[message] = timestamp
            return True
        else:
            if timestamp < x + 10:
                return False
            else:
                self.h[message] = timestamp
                return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
