class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        h = {"6": "9", "8": "8", "1": "1", "9": "6", "0": "0"}
        n1 = ["0", "1", "8"]
        ans = []
        def helper(n, l, r):
            if l and l[0] == "0":
                return
            elif n == 0:
                ans.append(l + r)
            elif n == 1:
                ans.extend([l + x + r for x in n1])
            else:
                for k in h:
                    helper(n - 2, l + k, h[k] + r)
        helper(n, "", "")
        return ans
        
