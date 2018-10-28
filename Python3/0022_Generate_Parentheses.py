class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def recurse(s = "", l = 0, r = 0):
            if len(s) == 2 * n:
                ans.append(s)
            if l < n:
                recurse(s + "(", l + 1, r)
            if r < l:
                recurse(s + ")", l, r + 1)
        recurse()
        return ans
        
