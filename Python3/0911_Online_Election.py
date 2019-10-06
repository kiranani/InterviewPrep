class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.states = []
        m, l, count = 0, None, collections.defaultdict(int)
        for t, p in zip(times, persons):
            count[p] = c = count[p] + 1
            if c >= m:
                m = c
                if p != l:
                    l = p
                    self.states.append((t, l))
        self.n = len(self.states)
        

    def q(self, t: int) -> int:
        l, r = 0, self.n - 1
        while l <= r:
            m = (l + r) // 2
            if t == self.states[m][0]:
                return self.states[m][1]
            elif t < self.states[m][0]:
                r = m - 1
            else:
                l = m + 1
        return self.states[r][1]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
