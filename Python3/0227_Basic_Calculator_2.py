from operator import add, sub, mul, floordiv
class Solution:
    def calculate(self, s: str) -> int:
        ops = {"+": add, "-": sub, "*": mul, "/": floordiv}
        pri = {"+": 0, "-": 0, "*": 1, "/": 1}
        opers, vals = [], [0]
        i, n = 0, len(s)
        while i < n:
            c = s[i]
            if c.isdigit():
                j, v = i + 1, int(c)
                while j < n and s[j].isdigit():
                    v = 10 * v + int(s[j])
                    j += 1
                i = j - 1
                vals.append(v)
            elif c in ops:
                while opers and pri[c] <= pri[opers[-1]]:
                    right = vals.pop()
                    vals.append(ops[opers.pop()](vals.pop(), right))
                opers.append(c)
            i += 1
        while opers:
            right = vals.pop()
            vals.append(ops[opers.pop()](vals.pop(), right))
        return vals[-1]
        
        
