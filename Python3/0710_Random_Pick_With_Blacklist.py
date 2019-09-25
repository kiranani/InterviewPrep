class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        self.m = {}
        self.n = N - len(blacklist)
        j, s = 0, set(blacklist)
        blacklist.sort()
        for i in range(self.n, N):
            if i not in s:
                self.m[blacklist[j]] = i
                j += 1

    def pick(self) -> int:
        r = random.randint(0, self.n - 1)
        return self.m.get(r, r)


# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
