class Solution:
    def longestValidParentheses(self, s: str) -> int:
        mx, n, stk = 0, len(s), [-1]
        for i, c in enumerate(s):
            if c == "(":
                stk.append(i)
            else:
                stk.pop()
                if not stk:
                    stk.append(i)
                mx = max(mx, i - stk[-1])
        return mx
        
