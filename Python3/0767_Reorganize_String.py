class Solution:
    def reorganizeString(self, S: str) -> str:
        n, d = len(S), collections.Counter(S)
        d = sorted(d.items(), key=lambda x: x[1])
        if d[-1][-1] > (n + 1) // 2:
            return ""
        a = []
        for c, co in d:
            a.extend(c * co)
        s = [None] * n
        s[::2], s[1::2] = a[n // 2:], a[:n // 2]
        return "".join(s)
