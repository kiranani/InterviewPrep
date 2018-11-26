class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n, ans = len(nums), set()
        def recurse(arr, ind):
            #print(arr, ind)
            ans.add(tuple(arr))
            if ind < n:
                for i in range(ind, n):
                    recurse(arr + (nums[i],), i + 1)
        recurse((), 0)
        return [list(x) for x in ans]
        
