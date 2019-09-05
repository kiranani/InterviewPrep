class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        if not num:
            return True
        h = {"6": "9", "0": "0", "8": "8", "1": "1", "9": "6"}
        i, n = 0, len(num)
        j = (n + 1) // 2
        while i < j:
            v = h.get(num[i])
            if not v or v != num[n - i - 1]:
                return False
            i += 1
        return True
        
