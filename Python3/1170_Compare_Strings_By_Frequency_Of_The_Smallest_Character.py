class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(word):
            d = collections.Counter(word)
            return d[min(d.keys())]
        def bs(t):
            l, r = 0, n - 1
            while l <= r:
                m = (l + r + 1) // 2
                if t >= words[m]:
                    l = m + 1
                else:
                    r = m - 1
            return r
        n, h = len(words), collections.defaultdict(list)
        for i, query in enumerate(queries):
            h[f(query)].append(i)
        words = sorted([f(x) for x in words])
        ans = [0] * len(queries)
        for k in h:
            i = n - 1 - bs(k)
            for j in h[k]:
                ans[j] = i
        return ans
        
