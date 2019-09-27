from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def getDiffs(s):
            l = [0] * (len(s) - 1)
            for i in range(1, len(s)):
                l[i - 1] = (ord(s[i - 1]) - ord(s[i])) % 26
            return tuple(l)
        h = defaultdict(lambda: defaultdict(list))
        for string in strings:
            h[len(string)][getDiffs(string)].append(string)
        ans = []
        for l in h:
            for t in h[l]:
                ans.append(h[l][t])
        return ans
        
