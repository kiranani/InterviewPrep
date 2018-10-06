class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        def permute(S, index, ans):
            if index < len(S):
                if S[index].isalpha():
                    n = len(ans)
                    for i in range(n):
                        ans[i][index] = ans[i][index].lower()
                        ans.append(ans[i][:])
                        ans[-1][index] = ans[-1][index].upper()
                permute(S, index + 1, ans)
        ans = [list(S)]      
        permute(list(S), 0, ans)
        return ["".join(x) for x in ans]
