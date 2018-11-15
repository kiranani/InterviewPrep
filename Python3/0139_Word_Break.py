class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        if n == 0:
            return True
        w, m = set(wordDict), [True] + [False] * n
        for j in range(1, n + 1):
            for i in range(j):
                #print(i, j, m[i])
                if m[i] and s[i:j] in w:
                    m[j] = True
                    break
        #print(m)
        return m[-1]
        
