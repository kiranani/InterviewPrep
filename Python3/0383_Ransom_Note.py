class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        n, m = collections.Counter(ransomNote), collections.Counter(magazine)
        return all(n[c] <= m[c] for c in n)
        
