class Solution:
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n, ans = len(nums), []
        def dfs(index, tmp):
            if len(tmp) > 1:
                #print(index, tmp)
                ans.append(tmp)
            seen = set()
            for i in range(index, n):
                if nums[i] not in seen:
                    seen.add(nums[i])
                    if len(tmp) > 0 and nums[i] >= tmp[-1]:
                        dfs(i + 1, tmp + [nums[i]])
                    elif len(tmp) == 0:
                        dfs(i + 1, [nums[i]])
        dfs(0, [])
        return ans
        
