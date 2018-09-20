class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        a, b = A.split(), B.split()
        h = {}
        for x in a:
            h[x] = h.get(x, 0) + 1
        for x in b:
            h[x] = h.get(x, 0) + 1
        
        return[x for x in h if h[x] == 1]
        
