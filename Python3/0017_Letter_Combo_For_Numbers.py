class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        h = {"2": "abc", "3": "def", "4": "ghi", "9": "wxyz",
             "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv"}
        n, ans = len(digits), []
        def recurse(i, s = ""):
            if i == n:
                ans.append(s)
                return
            for l in h[digits[i]]:
                recurse(i + 1, s + l)
        recurse(0)
        return ans if n > 0 else []
        
