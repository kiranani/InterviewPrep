from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []
        h = Counter(p)
        ans, count = [], len(h)
        for i, c in enumerate(s):
            if c in h:
                h[c] -= 1
                if h[c] == 0:
                    count -= 1
            if i >= np:
                lc = s[i - np]
                if lc in h:
                    h[lc] += 1
                if h[lc] > 0:
                    count += 1
            if count == 0:
                ans.append(i - np + 1)
        return ans
        
        
        
