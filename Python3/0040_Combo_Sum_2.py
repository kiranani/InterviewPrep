class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans = set()
        def recurse(a, rem, i):
            if rem == 0:
                ans.add(a)
                return
            for j, num in enumerate(candidates[i:]):
                if num <= rem:
                    recurse(a + (num,), rem - num, i + j + 1)
                else:
                    break
        recurse((), target, 0)
        ans = [list(x) for x in ans]
        return ans
        
