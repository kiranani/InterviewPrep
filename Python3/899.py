class Solution:
    def orderlyQueue(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        def minInd(a):
            mc, mi = a[0], 0
            for j in range(1, len(a)):
                if a[j] < mc:
                    mc, mi = a[j], j
            return mc
        S = list(S)
        if K > 1:
            S.sort()
            return "".join(S)
        n = len(S)
        minC = minInd(S)
        indices = [i for i, c in enumerate(S) if c == minC]        
        return min("".join(S[i:] + S[:i]) for i in indices)
      
     
