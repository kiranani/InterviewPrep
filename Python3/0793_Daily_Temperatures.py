class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0 for _ in range(len(T))]
        s = []
        for i, t in enumerate(T):
            while s and T[s[-1]] < t:
                li = s.pop()
                ans[li] = i - li
            s.append(i)
        return ans
        
