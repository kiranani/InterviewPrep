class Solution:
    def generateTheString(self, n: int) -> str:
        if n & 1 == 1:
            return "a" * n
        else:
            return "a" * (n - 1) + "b"
        
