class Solution:
    def expand(self, S: str) -> List[str]:
        n = len(S)
        def backtrack(i):
            if i == n:
                return [""]
            ans, prefix = [], []
            if S[i] == "{":
                while S[i] != "}":
                    prefix.append(S[i + 1])
                    i += 2
                i += 1
            else:
                j = i
                while j < n and S[j] != "{":
                    j += 1
                prefix.append(S[i:j])
                i = j
            suffix = backtrack(i)
            for pre in prefix:
                for suf in suffix:
                    ans.append(pre + suf)
            return ans
        return sorted(backtrack(0))
                
