class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n, ans = len(s), []
        def helper(arr, dots, i):
            if i == n:
                if dots == -1:
                    ans.append(".".join(arr))
            elif n - i <= 3 * (dots + 1) and n - i > dots:
                if s[i] == "0":
                    arr.append("0")
                    helper(arr, dots - 1, i + 1)
                    arr.pop()
                else:
                    for j in range(i, n - dots):
                        if int(s[i:j + 1]) < 256:
                            arr.append(s[i:j + 1])
                            helper(arr, dots - 1, j + 1)
                            arr.pop()
        helper([], 3, 0)
        return ans
        
