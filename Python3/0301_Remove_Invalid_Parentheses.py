class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        n, r, l = len(s), 0, 0
        for ch in s:
            if ch == "(":
                l += 1
            elif ch == ")":
                if l:
                    l -= 1
                else:
                    r += 1
        def recurse(i, rl, rr, l, r, acc):
            if i == n:
                if not rl and not rr:
                    ans.add("".join(acc))
            else:
                if (s[i] == "(" and rl) or (s[i] == ")" and rr):
                    recurse(i + 1, rl - (s[i] == "("), rr - (s[i] == ")"), l, r, acc)
                acc.append(s[i])
                if s[i] != "(" and s[i] != ")":
                    recurse(i + 1, rl, rr, l, r, acc)
                elif s[i] == "(":
                    recurse(i + 1, rl, rr, l + 1, r, acc)
                elif s[i] == ")" and l > r:
                    recurse(i + 1, rl, rr, l, r + 1, acc)
                acc.pop()
        ans = set()
        recurse(0, l, r, 0, 0, [])
        return list(ans)
        
