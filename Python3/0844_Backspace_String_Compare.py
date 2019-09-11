class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def get_str(s):
            a = []
            for c in s:
                if c != "#":
                    a.append(c)
                elif a:
                    a.pop()
            return "".join(a)
        return get_str(S) == get_str(T)
