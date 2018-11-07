class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        A, Z, c = ord("A"), ord("Z"), 0
        for l in word:
            if A <= ord(l) <= Z:
                c += 1
        return c in [0, len(word)] or (c == 1 and A <= ord(word[0]) <= Z)
     
