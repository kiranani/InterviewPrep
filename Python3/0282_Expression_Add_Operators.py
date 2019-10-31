from operator import add, sub, mul
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n, ans = len(num), []
        def backtrack(i, prev, curr, exp):
            if i == n:
                if curr == target:
                    ans.append("".join(exp))
            else:
                for j in range(i + 1, n + 1):
                    val = num[i:j]
                    if j == i + 1 or num[i] != "0":
                        if exp:
                            exp.extend(["+", val])
                            backtrack(j, int(val), curr + int(val), exp)
                            exp.pop(); exp.pop()
                            exp.extend(["-", val])
                            backtrack(j, -int(val), curr - int(val), exp)
                            exp.pop(); exp.pop()
                            exp.extend(["*", val])
                            backtrack(j, prev * int(val), curr - prev + prev * int(val), exp)
                            exp.pop(); exp.pop()
                        else:
                            exp.append(val)
                            backtrack(j, int(val), int(val), exp)
                            exp.pop()
        backtrack(0, 0, 0, [])
        return ans
            
            
