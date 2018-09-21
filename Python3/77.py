class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def recurse(i, n, k):
            if n - i == k - 1:
                return [list(range(i, n + 1))]
            elif k == 1:
                return [[x] for x in range(i, n + 1)]
            combs = []
            for i in range(i, n):
                down = recurse(i + 1, n, k - 1)
                down = [[i] + x for x in down]
                combs.extend(down)
            return combs;
        
        return recurse(1, n, k)
      
