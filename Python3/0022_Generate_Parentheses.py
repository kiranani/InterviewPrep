class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(l, r, exp):
            if l == r == n:
                ans.append("".join(exp))
                return
            exp.append("(")
            if l < n:
                backtrack(l + 1, r, exp)
            if r < l:
                exp[-1] = ")"
                backtrack(l, r + 1, exp)
            exp.pop()
        backtrack(0, 0, [])
        return ans
                
