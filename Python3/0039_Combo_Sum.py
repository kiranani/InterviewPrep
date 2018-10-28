class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans = []
        def recurse(a, rem, i):
            if rem == 0:
                ans.append(a)
                return
            for j, candidate in enumerate(candidates[i:]):
                if candidate <= rem:
                    recurse(a + [candidate], rem - candidate, i + j)
                else:
                    break
        recurse([], target, 0)
        return ans if target > 0 else []
