class Solution:

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w, self.n = w, len(w)
        for i in range(1, self.n):
            self.w[i] += self.w[i - 1]
        

    def pickIndex(self):
        """
        :rtype: int
        """
        i, j, r = 0, self.n - 1, random.randint(1, self.w[-1])
        while i <= j:
            m = (i + j) // 2
            if r == self.w[m]:
                return m
            elif r < self.w[m]:
                j = m - 1
            else:
                i = m + 1
        return i
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
