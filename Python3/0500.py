class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        a, A = ord("a"), ord("A")
        chars = [0] * 26
        for c in "asdfghjkl":
            chars[ord(c) - a] = 1
        for c in "zxcvbnm":
            chars[ord(c) - a] = 2
        ans = []
        for word in words:
            c = ord(word[0])
            c = c - A if c - A < 26 else c - a
            x, inARow = chars[c], True
            for c in word[1:]:
                c = ord(c)
                c = c - A if c - A < 26 else c - a
                if x != chars[c]:
                    inARow = False
                    break
            if inARow:
                ans.append(word)
        return ans
        
