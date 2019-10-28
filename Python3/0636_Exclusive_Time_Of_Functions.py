class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans, stk = [0] * (n + 1), [[-1, 0]]
        for log in logs:
            f, se, t = log.split(":")
            f, t = int(f), int(t)
            if se == "start":
                ans[stk[-1][0]] += t - stk[-1][1]
                stk.append([f, t])
            else:
                t += 1
                ans[stk[-1][0]] += t - stk[-1][1]
                stk.pop()
                stk[-1][-1] = t
        ans.pop()
        return ans
                    
        
