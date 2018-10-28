class Solution:
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        ans, i = [], 0
        while i < n - k - 1:
            i += 1
            ans.append(i)
        j, iters = 0, (k + 1) // 2
        while j < iters:
            j += 1
            ans.extend([j + i, n - j + 1])
        if len(ans) < n:
            ans.append(i + j + 1)
        return ans
