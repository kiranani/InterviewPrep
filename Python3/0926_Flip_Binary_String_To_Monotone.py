class Solution:
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        n = len(S)
        ones, zeroes = [0] * n, [0] * n
        ones[0] = 1 if S[0] == "1" else 0
        zeroes[-1] = 1 if S[-1] == "0" else 0
        for i in range(1, n):
            if S[i] == "1":
                ones[i] = ones[i - 1] + 1
            else:
                ones[i] = ones[i - 1]
            if S[-i - 1] == "0":
                zeroes[-i - 1] = zeroes[-i] + 1
            else:
                zeroes[-i - 1] = zeroes[-i]
        #print(ones)
        #print(zeroes)
        if ones[-1] == n or zeroes[0] == n:
            return 0
        ans = min(zeroes[0], ones[-1])
        for i in range(1, len(S)):
            ans = min(ans, zeroes[i]+ones[i-1])
        return ans
            
