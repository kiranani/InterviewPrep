class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        ans = []
        for word in words:
            if len(pattern) != len(word):
                continue
            s, h, match = set(), {}, True
            for i, x in enumerate(pattern):
                y = word[i]
                if h.get(x):
                    if h.get(x) != y:
                        match = False
                        break
                else:
                    if y not in s:
                        h[x] = y
                        s.add(y)
                    else:
                        match = False
                        break
            if match:
                ans.append(word)
        return ans
