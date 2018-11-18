class Solution:
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        a, b, n = sorted(enumerate(A), key = lambda x: x[1]), sorted(enumerate(B), key = lambda x: x[1]), len(A)
        ans, rem, j = [0] * n, [], 0
        for t in a:
            if t[1] <= b[j][1]:
                rem.append(t[1])
            else:
                ans[b[j][0]] = t[1]
                j += 1
        while j < n:
            ans[b[j][0]] = rem.pop()
            j += 1
        return ans
        
