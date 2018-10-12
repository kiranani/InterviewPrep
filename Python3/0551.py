class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            return True
        aCount, lCount, p1, p2 = 0, 0, s[0], s[1]
        if p1 == "A":
            aCount += 1
        elif p1 == "L":
            lCount += 1
        if p2 == "A":
            aCount += 1
            lCount = 0
        elif p2 == "L":
            lCount += 1
        else:
            lCount = 0
        for c in s[2:]:
            if c == "A":
                lCount = 0
                aCount += 1
            elif c == "L":
                lCount += 1
            else:
                lCount = 0
            if aCount > 1 or lCount > 2:
                return False
        return aCount < 2 and lCount < 3
        
