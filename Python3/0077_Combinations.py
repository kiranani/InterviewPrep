class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(i, res):
            if len(res) == k:
                ans.append(res)
                return
            for j in range(i + 1, n + 1):
                backtrack(j, res + [j])
        backtrack(0, [])
        return ans
        
