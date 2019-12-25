from collections import defaultdict
class WordDistance:

    def __init__(self, words: List[str]):
        self.d = defaultdict(list)
        for i, word in enumerate(words):
            self.d[word].append(i)
        

    def shortest(self, word1: str, word2: str) -> int:
        l1, l2 = self.d[word1], self.d[word2]
        n1, n2, i1, i2, mn = len(l1), len(l2), 0, 0, float("inf")
        while i1 < n1 and i2 < n2:
            mn = min(mn, abs(l1[i1] - l2[i2]))
            if l1[i1] < l2[i2]:
                i1 += 1
            else:
                i2 += 1
        return mn
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
