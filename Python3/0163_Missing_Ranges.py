class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ans, l = [], lower
        def updateAns(l, r, ans):
            if l == r:
                ans.append(str(l))
            elif l < r:
                ans.append(str(l) + "->" + str(r))
        
        for num in nums:
            if l < num:
                r = num - 1
                updateAns(l, r, ans)
            l = num + 1
        updateAns(l, upper, ans)
        return ans
        
