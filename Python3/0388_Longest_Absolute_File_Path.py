class Solution:
    def lengthLongestPath(self, input: str) -> int:
        i, n, h, m = 0, len(input), [], 0
        while i < n:
            l, c, f = 0, 0, False
            while i < n and input[i] == "\t":
                l, i = l + 1, i + 1
            while i < n and input[i] != "\n":
                if input[i] == ".": f = True
                c, i = c + 1, i + 1
            if len(h) <= l: h.append(c)
            else: h[l] = c
            if f:
                c = l + sum(h[:l + 1])
                m = max(m, c)
            i += 1
        return m
                
        
