from operator import add, sub, mul, floordiv
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        values, ops = [], {"+": add, "-": sub, "*": mul, "/": floordiv}
        for token in tokens:
            if token in ops:
                r, l = values.pop(), values.pop()
                if token == "/" and r * l < 0:
                    values.append(math.ceil(l / r))
                else:
                    values.append(ops[token](l, r))
            else:
                values.append(int(token))
        return values[-1]
        
