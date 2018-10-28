class Solution:
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def recurse(a):
            if len(a) == len(s):
                ans.add("".join(a))
                return
            for c in h:
                if h[c] > 0:
                    h[c] -= 2
                    recurse([c] + a + [c])
                    h[c] += 2

        h = collections.Counter(s)
        odds, evens = [], []
        for c in h:
            if h[c] % 2 == 1:
                odds.append(c)
            else:
                evens.append(c)
        if len(odds) > 1 or (len(odds) == 1 and len(s) % 2 == 0):
            return []
        ans, a = set(), []
        if len(odds) > 0:
            h[odds[0]] -= 1
            a = [odds[0]]
        recurse(a)
        return list(ans)
