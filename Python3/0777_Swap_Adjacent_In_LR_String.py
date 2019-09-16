class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        n = len(start)
        if n != len(end):
            return False
        sl, el = collections.deque(), collections.deque()
        for i, (s, e) in enumerate(zip(start, end)):
            if s != "X":
                sl.append((i, s))
            if e != "X":
                el.append((i, e))
            if sl and el:
                s, e = sl.popleft(), el.popleft()
                if s[1] != e[1]:
                    return False
                elif s[1] == "R" and s[0] > e[0]:
                    return False
                elif s[1] == "L" and s[0] < e[0]:
                    return False
        return not sl and not el
            
        
