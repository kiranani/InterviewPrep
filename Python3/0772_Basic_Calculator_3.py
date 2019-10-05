from operator import floordiv, mul, add, sub
class Solution:
    def calculate(self, s: str) -> int:
        ops = {"+": add, "-": sub, "*": mul, "/": floordiv}
        pri = {"+": 1, "-": 1, "*": 2, "/": 2}
        i, n = 0, len(s)
        def helper(i):
            values, opers = [0], []
            while i < n:
                c = s[i]
                if c.isdigit():
                    j = i
                    while j + 1 < n and s[j + 1].isdigit():
                        j += 1
                    values.append(int(s[i:j + 1]))
                    i = j
                elif c in ops:
                    while opers and pri[c] <= pri[opers[-1]]:
                        r, l = values.pop(), values.pop()
                        values.append(ops[opers.pop()](l, r))
                    opers.append(c)
                elif c == "(":
                    i, value = helper(i + 1)
                    values.append(value)
                elif c == ")":
                    break
                i += 1
            while opers and len(values) > 1:
                r, l = values.pop(), values.pop()
                values.append(ops[opers.pop()](l, r))
            return i, int(values[-1])
        return helper(0)[1]
        
