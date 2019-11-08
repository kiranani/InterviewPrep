class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        stk = []
        for c in expression:
            if c == "{" or c == ",":
                stk.append(c)
            elif c == "}":
                while stk[-2] == ",":
                    group = stk.pop()
                    stk.pop()
                    stk[-1] |= group
                final = stk.pop()
                stk[-1] = final
            else:
                stk.append(set(c))
            while len(stk) > 1 and isinstance(stk[-2], set) and isinstance(stk[-1], set):
                group1, group2 = stk.pop(), stk.pop()
                stk.append(set([b + a for a in group1 for b in group2]))
        return sorted(stk[-1])
                
