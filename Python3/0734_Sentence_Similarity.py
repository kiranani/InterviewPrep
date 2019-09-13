class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        n = len(words1)
        if n != len(words2):
            return False
        h = collections.defaultdict(set)
        for pair in pairs:
            h[pair[0]].add(pair[1])
            h[pair[1]].add(pair[0])
        for i in range(n):
            word1, word2 = words1[i], words2[i]
            if word2 not in h[word1] and word1 != word2:
                return False
        return True
        
