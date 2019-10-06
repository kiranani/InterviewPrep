class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        ans, s = [0] * n, []
        for i, t in enumerate(T):
            while s and t > T[s[-1]]:
                j = s.pop()
                ans[j] = i - j
            s.append(i)
        return ans
        
        
