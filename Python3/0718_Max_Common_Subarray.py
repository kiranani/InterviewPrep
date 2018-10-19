class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        nA, nB = len(A), len(B)
        dp = [[0] * (nB + 1) for i in range(nA + 1)]
        for i in range(nA):
            for j in range(nB):
                if A[i] == B[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
        return max(max(x) for x in dp)
