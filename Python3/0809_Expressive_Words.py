class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def get_counts(S):
            s, i, n = [], 0, len(S)
            while i < n:
                j = i + 1
                while j < n and S[i] == S[j]:
                    j += 1
                s.append((S[i], j - i))
                i = j
            return s
        c, sc = 0, get_counts(S)
        n = len(sc)
        for word in words:
            wc = get_counts(word)
            if len(wc) != n:
                continue
            valid = True
            for i in range(n):
                si, wi = sc[i], wc[i]
                if si[0] != wi[0] or si[1] < wi[1] or (si[1] > wi[1] and si[1] < 3):
                    valid = False
                    break
            c += (valid)
        return c
                
    
        
        
