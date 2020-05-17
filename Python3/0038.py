class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        s = self.countAndSay(n - 1)
        ans, ch, cnt = [], s[0], 1
        for c in s[1:]:
            if c != ch:
                ans.extend([str(cnt), ch])
                ch, cnt = c, 1
            else:
                cnt += 1
        ans.extend([str(cnt), ch])
        return "".join(ans)
        
