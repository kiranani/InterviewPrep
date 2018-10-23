class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        n = len(num)
        if n <= k:
            return "0"
        
        i, s = 0, []
        while i < n:
            while k > 0 and len(s) > 0 and s[-1] > num[i]:
                s.pop()
                k -= 1
            s.append(num[i])
            i += 1
        while k > 0:
            s.pop()
            k -= 1
        j = 0
        while j < len(s) and s[j] == "0":
            j += 1
        if j == len(s):
            return "0"
        return "".join(s[j:])
