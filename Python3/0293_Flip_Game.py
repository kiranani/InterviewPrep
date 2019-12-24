class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        n, ans = len(s), []
        for i in range(n - 1):
            if s[i] == s[i + 1] == "+":
                ans.append(s[:i] + "--" + s[i + 2:])
        return ans
        
