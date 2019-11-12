class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        n, ans = len(word), []
        def helper(i, c, exp):
            if i == n:
                ans.append("".join(exp))
            else:
                exp.append(word[i])
                helper(i + 1, 0, exp)
                exp.pop()
                if c > 0:
                    exp[-1] = str(c + 1)
                    helper(i + 1, c + 1, exp)
                    exp[-1] = str(c)
                else:
                    exp.append("1")
                    helper(i + 1, 1, exp)
                    exp.pop()
        helper(0, 0, [])
        return ans
        
