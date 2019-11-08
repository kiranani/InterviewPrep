class Solution:
    def numberToWords(self, num: int) -> str:
        parts = collections.deque()
        while num:
            num, mod = divmod(num, 1000)
            parts.appendleft(mod)
        denoms = {1: "Thousand", 2: "Million", 3: "Billion"}
        digits = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 
                  7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 
                  12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 
                  16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}
        tens = {2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 
                7: "Seventy", 8: "Eighty", 9: "Ninety", 10: "Hundred"}
        def getPart(num, ans):
            div, num = divmod(num, 100)
            if div:
                ans.extend([digits[div], tens[10]])
            if num and num < 20:
                ans.append(digits[num])
            elif num:
                div, mod = divmod(num, 10)
                ans.append(tens[div])
                if mod:
                    ans.append(digits[mod])
        if not parts:
            return "Zero"
        n, ans = len(parts), []
        for i, part in enumerate(parts):
            if part:
                getPart(part, ans)
                if n - 1 - i > 0:
                    ans.append(denoms[n - i - 1])
        return(" ".join(ans))
        
