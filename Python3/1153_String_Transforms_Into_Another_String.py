class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        h = {}
        for c1, c2 in zip(str1, str2):
            if c1 in h and h[c1] != c2:
                return False
            h[c1] = c2
        return len(set(str2)) < 26 or str1 == str2
            
