class Trie:
    def __init__(self, c):
        self.c = c
        self.end = False
        self.d = {}
        
    def insert(self, s):
        if len(s) == 0:
            self.end = True
        else:
            if s[0] not in self.d:
                self.d[s[0]] = Trie(s[0])
            self.d[s[0]].insert(s[1:])
            
    def find(self, s, c):
        if s and s[0] in self.d:
            m = self.d[s[0]].find(s[1:], c + 1)
            if self.end:
                m = max(m, c)
            return m
        elif self.end:
            return c
        else:
            return 0

class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        t = Trie("")
        for word in dict:
            t.insert(word)
        ans, interval = [], None
        for i in range(len(s)):
            c = t.find(s[i:], 0)
            if c:
                if interval and i - interval[1] < 1:
                    interval = interval[0], max(i + c, interval[1])
                else:
                    if interval:
                        ans.append("<b>" + s[interval[0]:interval[1]] + "</b>")
                    interval = i, i + c
            elif interval and i == interval[1]:
                ans.append("<b>" + s[interval[0]:interval[1]] + "</b>")
                interval = None
                ans.append(s[i])
            elif not interval:
                ans.append(s[i])
            if i + c == len(s): break
        if interval:
            ans.append("<b>" + s[interval[0]:interval[1]] + "</b>")
        return "".join(ans)
        
        
