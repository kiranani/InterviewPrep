class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        d = collections.Counter(words)
        return sorted(d, key=lambda x: (-d[x], x))[:k]
        
