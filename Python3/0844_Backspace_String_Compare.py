class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def get_char(s, i):
            hashes, chars, c = 0, 0, ""
            while i > -1:
                c = s[i]
                if c == "#":
                    hashes += 1
                else:
                    chars += 1
                i -= 1
                if chars - hashes == 1:
                    return i, c
            return -1, ""
        
        i, j = len(S) - 1, len(T) - 1
        while i > -1 or j > -1:
            (i, cs), (j, ct) = get_char(S, i), get_char(T, j)
            if cs != ct:
                return False
        return True
                
        
