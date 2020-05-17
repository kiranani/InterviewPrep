class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        i, i_max = 0, len(strs[0])
        while i < i_max:
            p = strs[0][i]
            for s in strs[1:]:
                if i >= len(s) or p != s[i]:
                    return strs[0][:i]
            i += 1
        return "".join(strs[0])
        
