class ValidWordAbbr:
    
    def getAbbr(word):
            n = len(word)
            if n < 3:
                return word
            else:
                return word[0] + str(n - 2) + word[-1]

    def __init__(self, dictionary: List[str]):
        self.d = collections.defaultdict(set)
        for word in dictionary:
            self.d[ValidWordAbbr.getAbbr(word)].add(word)
        

    def isUnique(self, word: str) -> bool:
        abbr = ValidWordAbbr.getAbbr(word)
        return (not self.d[abbr]
                or len(self.d[abbr]) == 1 and word in self.d[abbr])
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
