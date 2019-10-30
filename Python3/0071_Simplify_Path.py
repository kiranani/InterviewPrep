class Solution:
    def simplifyPath(self, path: str) -> str:
        path, stk, s = path + "/", [], ""
        for c in path:
            if c == "/":
                if s == "..":
                    if stk:
                        stk.pop()
                elif s and s not in ["/", "."]:
                    stk.append(s)
                s = ""
            else:
                s += c
        return "/" + "/".join(stk)
        
