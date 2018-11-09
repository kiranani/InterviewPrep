class RandomizedSet:

    def __init__(self):
        self.count = 0
        self.hash = {}
        self.array = []
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if self.hash.get(val) is not None:
            return False
        else:
            self.hash[val] = self.count
            self.array.append(val)
            self.count += 1
            return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        #print(self.array, val, self.hash.get(val))
        if self.hash.get(val) is not None:
            self.hash[self.array[-1]], self.array[self.hash[val]], self.array[-1] = self.hash[val], self.array[-1], self.array[self.hash[val]]
            del self.hash[val]
            self.array.pop()
            self.count -= 1
            return True
        else:
            return False         
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.array[random.randint(0, self.count - 1)]
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
