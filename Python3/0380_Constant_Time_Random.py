class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.h = {}
        self.l = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if self.h.get(val) is not None:
            return False
        self.h[val] = len(self.l)
        self.l.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if not self.h or self.h.get(val) is None:
            return False
        i = self.h[val]
        self.h[self.l[-1]] = i
        del self.h[val]
        self.l[i] = self.l[-1]
        self.l.pop()
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return len(self.l) and self.l[random.randint(0, len(self.l) - 1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
