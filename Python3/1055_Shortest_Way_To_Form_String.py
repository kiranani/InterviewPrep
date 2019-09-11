class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        ns, nt, d = len(source), len(target), collections.defaultdict(list)
        for i in range(ns):
            d[source[i]].append(i)
        def bs(l, t):
            if not l:
                return None
            i, j = 0, len(l) - 1
            while i <= j:
                m = (i + j) // 2
                if t == l[m]:
                    return m
                elif t < l[m]:
                    j = m - 1
                else:
                    i = m + 1
            return i if i < len(l) else -1
        ti, si, c = 0, -1, 1
        while ti < nt:
            ch = target[ti]
            si = bs(d[ch], si + 1)
            if si is None:
                return -1
            elif si == -1:
                c += 1
                si = -1
            else:
                si = d[ch][si]
                ti += 1
        return c
        
