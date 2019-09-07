class AutocompleteSystem:
    class Trie:
        def __init__(self, c):
            self.d = {}
            self.char = c
            self.ending = False
            self.count = 0
            
            
        def add(self, s, c):
            n = len(s)
            if n == 0:
                return
            tt = self.d.get(s[0])
            if not tt:
                tt = AutocompleteSystem.Trie(s[0])
                self.d[s[0]] = tt
            if n == 1:
                tt.ending = True
                tt.count += c
            tt.add(s[1:], c)
            
            
        def get_strs(self, s):
            strs = []
            if not s:
                for k in self.d:
                    strs.extend(self.d[k].get_strs(s))
                if self.ending:
                    strs.append((self.count, ""))
            elif self.d.get(s):
                strs = self.d[s].get_strs("")
            return [(x[0], self.char + x[1]) for x in strs]
        

    def __init__(self, sentences: List[str], times: List[int]):
        self.t = self.Trie("")
        for i, c in enumerate(times):
            self.t.add(sentences[i], c)
        self.s = ""
        self.results = []
        

    def input(self, c: str) -> List[str]:
        if len(self.s) == 0:
            self.s += c
            self.results = self.t.get_strs(c)
        elif c == "#":
            self.t.add(self.s, 1)
            self.s, self.results = "", []
        else:
            n = len(self.s)
            self.s += c
            self.results = [x for x in self.results if len(x[1]) > n and x[1][n] == c]
        self.results.sort(key=lambda x: (-x[0], x[1]))
        return [x[1] for x in self.results[:3]]
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
