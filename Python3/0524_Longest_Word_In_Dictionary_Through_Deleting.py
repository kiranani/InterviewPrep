class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def isSubstring(s1, s2):
            n1, n2 = len(s1), len(s2)
            i, j = 0, 0
            while i < n1 and j < n2 and n2 - j <= n1 - i:
                if s1[i] == s2[j]:
                    j += 1
                i += 1
            return j == n2
        best = ""
        for word in d:
            if isSubstring(s, word):
                if len(word) > len(best):
                    best = word
                elif len(word) == len(best):
                    best = min(best, word, key=lambda x: (-len(x), x))
        return best
