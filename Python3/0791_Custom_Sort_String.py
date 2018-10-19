class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        tDict = collections.Counter(T)
        ans = []
        for c in S:
            ans.extend([c] * tDict.pop(c, 0))
        for c in tDict:
            ans.extend([c] * tDict.get(c))
        return "".join(ans)
