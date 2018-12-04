class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        if not n:
            return []
        ans, stk = [0] * n, []
        for log in logs:
            i, se, t = log.split(":")
            i, t = int(i), int(t)
            if se == "start":
                if stk:
                    ans[stk[-1][0]] += t - stk[-1][1]
                    stk[-1][1] = t - stk[-1][1]
                stk.append([i, t])
            else:
                e = stk.pop()
                if stk:
                    stk[-1][1] = t + 1
                ans[e[0]] += t + 1 - e[1]
        return ans
        
