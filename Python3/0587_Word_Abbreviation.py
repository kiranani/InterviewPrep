class Solution:
    def wordsAbbreviation(self, dict: List[str]) -> List[str]:
        def getAbbr(s, i):
            if len(s) - i < 4:
                return s, i
            return s[:i + 1] + str(len(s) - 2 - i) + s[-1], i
        groups = collections.defaultdict(list)
        for i, word in enumerate(dict):
            groups[getAbbr(word, 0)].append(i)
        a = [None] * len(dict)
        while groups:
            t = collections.defaultdict(list)
            for k, v in groups.items():
                if len(v) == 1:
                    a[v[0]] = k[0]
                else:
                    for i in v:
                        t[getAbbr(dict[i], k[1] + 1)].append(i)
            groups = t
        return a
