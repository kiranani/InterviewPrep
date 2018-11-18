class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        n = len(S)
        i, j, ans = 0, n, []
        for s in S:
            if s == "D":
                ans.append(j)
                j -= 1
            else:
                ans.append(i)
                i +=1
        ans.append(i)
        return ans
        
