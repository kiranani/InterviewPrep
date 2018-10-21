class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        elif num == 1:
            return [0, 1]
        else:
            ans, c = [0, 1], 1
            for n in range(2, num + 1):
                if n & (n - 1) == 0:
                    ans.append(1)
                    c = 1
                else:
                    ans.append(1 + ans[c])
                    c += 1
            return ans
