class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        def recurse(arr, s, num):
            if s > n or (s == n and len(arr) != k):
                return
            elif s == n:
                ans.append(arr)
            else:
                for x in range(num, 10):
                    recurse(arr + [x], s + x, x + 1)
        recurse([], 0, 1)
        return ans
    
