class Solution:
    def solveEquation(self, equation: str) -> str:
        lhs, rhs, t = [0, 0], [0, 0], []
        side = lhs
        for c in equation + "+":
            if c in ["+", "-", "="]:
                if t and t[-1] == "x":
                    t.pop()
                    if not t or t[-1] in ["+", "-"]:
                        t.append("1")
                    side[0] += int("".join(t))
                elif t:
                    side[1] += int("".join(t))
                if c == "=":
                    t, side = [], rhs
                else:
                    t = [c]
            else:
                t.append(c)
        x, c = lhs[0] - rhs[0], rhs[1] - lhs[1]
        if x == 0:
            if c == 0:
                return "Infinite solutions"
            return "No solution"
        else:
            return "x=" + str(c // x)
        
