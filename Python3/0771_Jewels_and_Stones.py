class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jSet = set(J)
        c = 0
        for s in S:
            if s in jSet:
                c += 1
        return c
        
